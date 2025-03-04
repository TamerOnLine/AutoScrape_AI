import sys
import os

# إضافة مجلد src إلى sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from tools.web_scraper_tool import web_scraper_tool



result = web_scraper_tool.func("https://medlineplus.gov/genetics/condition/pyridoxine-dependent-epilepsy/")
print(result)
