import sys
import os

# إضافة مجلد src إلى sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from tools.advanced_web_scraper import scrape_webpage_selenium

def test_scrape_webpage_selenium():
    url = "https://example.com"
    result = scrape_webpage_selenium(url)
    print(result)  # تحقق من النتيجة المتوقعة

if __name__ == "__main__":
    test_scrape_webpage_selenium()

