"""
QUESTION:
Convert a camelCase string to snake_case notation. The function, `convert_to_snake_case`, should take a string as input and return a new string where all words start with a lowercase letter and an underscore is added before each uppercase letter from the original string.
"""

def convert_to_snake_case(camelCaseString):
    snake_case_string = ""
    for char in camelCaseString:
        if char.isupper():
            snake_case_string += "_" + char.lower()
        else:
            snake_case_string += char
    return snake_case_string.lstrip("_")