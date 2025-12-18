"""
QUESTION:
Write a function called `validate_pattern` that takes two parameters: `pattern` (dict) and `input_dict` (dict). The `pattern` dictionary represents the expected pattern, where the keys are strings representing the expected keys and the values are types representing the expected value types. The function should return `True` if the `input_dict` matches the specified pattern, i.e., all keys in the `pattern` exist in `input_dict` and their corresponding values are of the expected types; otherwise, it should return `False`.
"""

def validate_pattern(pattern: dict, input_dict: dict) -> bool:
    for key, value_type in pattern.items():
        if key not in input_dict or not isinstance(input_dict[key], value_type):
            return False
    return True