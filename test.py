import os
import json
import main

# Test Chinese
os.environ["LANGUAGE"] = "zh"
main.LANGUAGE = "zh"
print("=== 中文输出 (zh) ===")
zh_data = main.get_weather_data("Ottawa")
print(json.dumps(zh_data, indent=2, ensure_ascii=False))

print("\n")

# Test English
os.environ["LANGUAGE"] = "en"
main.LANGUAGE = "en"
print("=== 英文输出 (en) ===")
en_data = main.get_weather_data("Ottawa")
print(json.dumps(en_data, indent=2, ensure_ascii=False))
