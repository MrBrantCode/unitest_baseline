"""
QUESTION:
Create a function named `contains_substring` that takes two strings, `string1` and `string2`, as input. The function should check if `string1` contains `string2` as a substring, ignoring case sensitivity and whitespace characters. If `string1` contains any non-alphabetic or non-whitespace characters, the function should return False. The function should also return False if either `string1` or `string2` has leading or trailing whitespace characters. The function should not use built-in string matching functions or regular expressions.
"""

def contains_substring(string1, string2):
    string1 = string1.strip()
    string2 = string2.strip()

    if string1 != string1.strip() or string2 != string2.strip():
        return False

    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")

    for char in string1:
        if not char.isalpha() and char != " ":
            return False

    string1 = string1.lower()
    string2 = string2.lower()

    return string2 in string1