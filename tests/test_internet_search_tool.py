import sys
import os

# إضافة مجلد src إلى sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from tools.internet_search_tool import search_internet

def test_search_internet():
    query = "LangChain"
    result = search_internet(query)
    print(result)  # تحقق من النتيجة المتوقعة

if __name__ == "__main__":
    test_search_internet()



