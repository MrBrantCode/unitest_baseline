"""
QUESTION:
Implement a function named `snake_case_converter` that takes a string `s` as input and returns the string converted to snake_case. The conversion should ignore any special characters or numbers, maintain only lowercase letters, and handle multiple spaces between words. No external libraries or built-in functions are allowed except basic string manipulation techniques.
"""

def snake_case_converter(s):
    result = ""
    for c in s:
        if c.isalpha():
            result += c.lower()
        elif c.isspace() and len(result) != 0 and result[-1] != '_':
            result += "_"
    if result[-1] == "_":
        result = result[:-1]
    return result