import sys
import os
import unittest

# إضافة src إلى المسار لضمان استيراد الأدوات
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
print("🔍 Current sys.path:", sys.path)  # التحقق من المسارات المحملة

from tools.auto_scraper_tool import scrape_and_store

# تحميل متغيرات البيئة
from dotenv import load_dotenv
load_dotenv()

# التحقق من وجود API Key
api_key = os.getenv("PINECONE_API_KEY")
if api_key:
    print("✅ PINECONE_API_KEY is loaded successfully!")
else:
    print("❌ PINECONE_API_KEY is missing!")

# تعريف الاختبار
class TestAutoScraperTool(unittest.TestCase):
    def test_scrape_and_store(self):
        test_url = "https://medlineplus.gov/healthtopics.html"
        result = scrape_and_store(test_url)
        self.assertIn("Data extracted from", result)

if __name__ == "__main__":
    unittest.main()
