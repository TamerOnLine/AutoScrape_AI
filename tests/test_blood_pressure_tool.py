import sys
import os

# إضافة مجلد src إلى sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from tools.blood_pressure_tool import search_blood_pressure_diseases

def test_search_blood_pressure_diseases():
    query = "hypertension"
    result = search_blood_pressure_diseases(query)
    print(result)  # تحقق من النتيجة المتوقعة

if __name__ == "__main__":
    test_search_blood_pressure_diseases()
