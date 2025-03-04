import os
import logging

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from pinecone import Pinecone, ServerlessSpec
from langchain.tools import Tool
#from langchain_community.embeddings import OpenAIEmbeddings

from sentence_transformers import SentenceTransformer






# Initialize Pinecone
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY is missing. Please check your .env file.")

pc = Pinecone(api_key=PINECONE_API_KEY)

# List available indexes
existing_indexes = pc.list_indexes()
index_names = [idx["name"] for idx in existing_indexes]

# Index name
INDEX_NAME = "my-index"

# Check if the index exists, otherwise create it
if INDEX_NAME not in index_names:
    logging.info(f"Index '{INDEX_NAME}' not found. Creating a new one...")
    pc.create_index(
        name=INDEX_NAME,
        dimension=1536,
        metric="euclidean",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    logging.info(f"Index '{INDEX_NAME}' created successfully.")

# Retrieve index for use
index = pc.Index(INDEX_NAME)
logging.info(f"Using index: {INDEX_NAME}")

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class AutoScraperSpider(scrapy.Spider):
    """Scrapy spider to fetch and process webpage content."""
    name = "auto_scraper"

    def __init__(self, url: str = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url] if url else []

    def parse(self, response):
        """Extract text from the webpage and store it in Pinecone."""
        paragraphs = response.css("p::text").getall()
        extracted_text = " ".join(paragraphs)

        if extracted_text:
            self.store_in_pinecone(extracted_text)

    def store_in_pinecone(self, content: str):
        """Convert content to vectors and store it in Pinecone."""
        if len(content) > 5000:
            content = content[:5000]  # Prevent exceeding token limits

        #embeddings = OpenAIEmbeddings().embed_query(content)
        model = SentenceTransformer("all-MiniLM-L6-v2")  # نموذج سريع وخفيف الوزن
        embeddings = model.encode(content)
        index.upsert(vectors=[("web_content", embeddings, {"text": content})])
        logging.info("Data successfully stored in Pinecone.")


def scrape_and_store(url: str) -> str:
    """Run Scrapy and store extracted data in Pinecone."""
    if not url:
        return "URL is required for scraping."

    process = CrawlerProcess(get_project_settings())
    process.crawl(AutoScraperSpider, url=url)
    process.start()
    return f"Data extracted from {url} and stored in Pinecone."


# Register the tool in LangChain
auto_scraper_tool = Tool(
    name="AutoScraperTool",
    func=scrape_and_store,
    description="Scrapes web content using Scrapy and stores it in Pinecone for vector-based search.",
    return_direct=True,
)

# Ensure `loaded_tools` is defined
if "loaded_tools" not in globals():
    loaded_tools = []
loaded_tools.append(auto_scraper_tool)

logging.info(" AutoScraperTool successfully registered.")
