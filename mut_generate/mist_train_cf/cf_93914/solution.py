"""
QUESTION:
Create a function called `parse_and_display_json` that takes a JSON string as input. This function should parse the JSON string, validate its structure, and display its contents, including nested objects and arrays. The function should also handle custom data types such as dates in the format "YYYY-MM-DD" and complex numbers in the format "a+bj" where a and b are integers. If a date string is encountered, it should be displayed in the format "DD/MM/YYYY". If a complex number is encountered, it should be displayed as "a + bj". If the JSON string has an invalid structure, the function should print "Invalid JSON structure".
"""

import json
from datetime import datetime

def parse_and_display_json(json_str):
    try:
        parsed_json = json.loads(json_str)
    except json.JSONDecodeError:
        print("Invalid JSON structure")
        return

    def display_json(data):
        if isinstance(data, dict):
            for key, value in data.items():
                print(key)
                display_json(value)
        elif isinstance(data, list):
            for item in data:
                display_json(item)
        elif isinstance(data, str):
            try:
                date = datetime.strptime(data, "%Y-%m-%d")
                print(f"Date: {date.strftime('%d/%m/%Y')}")
            except ValueError:
                try:
                    complex_num = complex(data.replace('j', 'j'))
                    print(f"Complex Number: {complex_num.real} + {complex_num.imag}j")
                except ValueError:
                    print(data)
        else:
            print(data)

    display_json(parsed_json)