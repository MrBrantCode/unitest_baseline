"""
QUESTION:
Implement a function named `find_true_keys` that takes a nested JSON object as input and returns a list of all keys with boolean values set to `True`, considering all levels of nesting. The function should only return the keys that have a boolean value of `True`, without considering the structure of the nested objects or arrays.
"""

def find_true_keys(json_obj: dict) -> list:
    true_keys = []

    def process_json(obj, prefix=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, bool) and value:
                    true_keys.append(prefix + key)
                elif isinstance(value, (dict, list)):
                    process_json(value, prefix + key + ".")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                process_json(item, prefix + str(i) + ".")

    process_json(json_obj)
    return true_keys