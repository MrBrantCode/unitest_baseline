"""
QUESTION:
Write a function called `parse_json` that takes a string representing a valid JSON object as input, where the JSON object contains only numeric values with no nested objects or arrays. The function should return the sum of all integer values in the JSON data without using any built-in JSON parsing library, instead implementing its own parsing algorithm.
"""

def parse_json(json_str):
    total_sum = 0
    number = ""
    is_negative = False

    for char in json_str:
        if char == '-':
            is_negative = True
        elif char.isdigit():
            number += char
        elif char == ',' or char == '}':
            if number:
                total_sum += int(number) * (-1 if is_negative else 1)
                number = ""
                is_negative = False

    return total_sum