"""
QUESTION:
Write a method named `is_substring` that takes two strings as input, `string1` and `string2`, and returns a boolean indicating whether `string1` contains `string2` as a substring. The method should ignore case sensitivity and whitespace characters, but return False if any special character is found in `string1`. Special characters include any non-alphabetic or non-whitespace character. The method cannot use any built-in string matching functions or regular expressions.
"""

def is_substring(string1, string2):
    # Remove whitespace and convert both strings to lowercase
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    # Check if any special character is present in string1
    for char in string1:
        if not char.isalpha() and not char.isspace():
            return False

    # Check if string2 is a substring of string1
    index = 0
    while index <= len(string1) - len(string2):
        if string1[index:index+len(string2)] == string2:
            return True
        index += 1

    return False