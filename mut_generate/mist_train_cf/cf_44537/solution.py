"""
QUESTION:
Create a function `parse_to_dict` that takes a string of comma-separated key-value pairs as input and returns a dictionary where the keys are the values before the "=" sign and the values are the values after the "=" sign. If a pair does not contain an "=", it should be ignored. The function should also handle cases where there are leading or trailing spaces around the "=" sign or between key-value pairs. If the input string is empty or does not contain any valid key-value pairs, the function should return an empty dictionary.
"""

def parse_to_dict(string):
    result_dict = {}
    pairs = string.split(", ")
    for pair in pairs:
        if "=" in pair:
            parts = pair.split("=")
            key = parts[0].strip()
            value = parts[1].strip()
            result_dict[key] = value
    return result_dict