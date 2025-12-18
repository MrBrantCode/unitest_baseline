"""
QUESTION:
Create a function named `display_json` that takes a string representing a JSON document as input. The function should parse the JSON document, validate its structure, and display its contents in a readable format, handling nested JSON objects and arrays. If the JSON structure is invalid, it should display an error message.
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