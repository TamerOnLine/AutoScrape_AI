import sys
import os

# إضافة مجلد src إلى sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from tools.stock_tool import get_stock_price

def test_get_stock_price():
    # اختبار السهم لشركة معروفة مثل Apple
    result = get_stock_price("AAPL")
    print(result)  # تحقق من النتيجة المتوقعة

if __name__ == "__main__":
    test_get_stock_price()


