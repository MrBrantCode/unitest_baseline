"""
QUESTION:
Write a function `get_name` that retrieves the value of the key "name" from a given JSON object. The function should handle nested JSON objects and return the value of the key "name" even if it is nested multiple levels deep. If the key "name" does not exist in the JSON object, the function should return None.
"""

def get_name(data):
    if "name" in data:
        return data["name"]
    elif isinstance(data, dict):
        for key in data:
            result = get_name(data[key])
            if result is not None:
                return result
    return None