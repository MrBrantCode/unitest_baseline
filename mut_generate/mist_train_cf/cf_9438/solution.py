"""
QUESTION:
Define a function named `display_json` that takes a JSON document as a string and displays its contents. The function should handle nested JSON objects and arrays, and it should validate the JSON structure. If the structure is invalid, the function should display an error message instead of the contents. The function should not return any value; it should only print the contents or the error message.
"""

import json

def display_json(json_data):
    # Load the JSON document
    try:
        data = json.loads(json_data)
    except json.JSONDecodeError as e:
        print("Invalid JSON structure:", e)
        return

    # Display the contents
    def display_content(data, indent=0):
        if isinstance(data, dict):
            for key, value in data.items():
                print("  " * indent, key, ":")
                display_content(value, indent + 1)
        elif isinstance(data, list):
            for item in data:
                display_content(item, indent)
        else:
            print("  " * indent, data)

    display_content(data)