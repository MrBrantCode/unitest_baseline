"""
QUESTION:
Write a function `camel_to_space` that takes a camel case string as input and returns the string with spaces separating the words. The input string will only contain uppercase and lowercase letters, and the function should not use any built-in string manipulation functions or methods.
"""

def camel_to_space(camel_str):
    result = ""
    for i in range(len(camel_str)):
        if camel_str[i].isupper() and i != 0:
            result += " " + camel_str[i].lower()
        else:
            result += camel_str[i]
    return result