"""
QUESTION:
Create a function called `extract_info` that takes a string `data` as input, where `data` contains multiple JSON objects representing key-value pairs. Extract the values associated with the keys "NUMBER", "EMOJI", "DOUBLE_QUOTED_WORD", and "SINGLE_QUOTED_WORD" from the JSON objects and return them in a dictionary with the corresponding keys. The values should be stored in lists. The input string is almost a valid JSON list, but it is missing the outer square brackets, and each JSON object may end with a comma. The function should handle these issues and also be able to handle cases where the input string is not a valid JSON.
"""

import json

def extract_info(data):
    extracted_values = {
        "NUMBER": [],
        "EMOJI": [],
        "DOUBLE_QUOTED_WORD": [],
        "SINGLE_QUOTED_WORD": []
    }

    data = data.strip().strip(',')  # Remove leading/trailing whitespace and commas
    data = '[' + data + ']'  # Enclose the data in square brackets to make it a valid JSON list

    try:
        json_data = json.loads(data)
        for item in json_data:
            if "NUMBER" in item:
                extracted_values["NUMBER"].append(item["NUMBER"])
            if "EMOJI" in item:
                extracted_values["EMOJI"].append(item["EMOJI"])
            if "DOUBLE_QUOTED_WORD" in item:
                extracted_values["DOUBLE_QUOTED_WORD"].append(item["DOUBLE_QUOTED_WORD"])
            if "SINGLE_QUOTED_WORD" in item:
                extracted_values["SINGLE_QUOTED_WORD"].append(item["SINGLE_QUOTED_WORD"])
    except json.JSONDecodeError:
        print("Invalid JSON format")

    return extracted_values