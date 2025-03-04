import sys
import os

# إضافة مجلد src إلى sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from tools.weather_tool import get_weather

def test_get_weather():
    # اختبار مدينة معروفة
    result = get_weather("Berlin")
    print(result)  # تحقق من النتيجة المتوقعة
    
if __name__ == "__main__":
    test_get_weather()

