"""
QUESTION:
Implement a function named `get_price(json_str)` that takes a string representing a JSON object as input and returns the value of the 'price' variable. The function should not use any built-in JSON parsing functions or libraries and should handle potential errors or edge cases.
"""

def get_price(json_str):
    stack = []
    current_dict = {}
    key = ''
    value = ''
    is_string = False

    for char in json_str:
        if char == '{':
            stack.append(current_dict)
            current_dict = {}
        elif char == '}':
            if key:
                current_dict[key] = value
                key = ''
                value = ''
            if stack:
                prev_dict = stack.pop()
                prev_dict.update(current_dict)
                current_dict = prev_dict
        elif char == '"':
            is_string = not is_string
        elif char == ':':
            pass
        elif char == ',':
            if key:
                current_dict[key] = value
                key = ''
                value = ''
        elif is_string:
            value += char
        else:
            if char != ' ':
                key += char

    try:
        return current_dict['price']
    except (KeyError, TypeError, IndexError):
        return None