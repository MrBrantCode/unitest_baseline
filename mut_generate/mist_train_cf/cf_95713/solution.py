"""
QUESTION:
Implement a function named `replace_values` that takes two parameters: a string and a dictionary of values. Replace the placeholders in the string with the values from the dictionary, where `%s` is for strings, `%d` for integers, and `%f` for floats, without using the str.format() method or any other string formatting libraries.
"""

def replace_values(string, values):
    for key, value in values.items():
        if isinstance(value, str):
            string = string.replace("%s", value, 1)
        elif isinstance(value, int):
            string = string.replace("%d", str(value), 1)
        elif isinstance(value, float):
            string = string.replace("%f", str(value), 1)
    return string