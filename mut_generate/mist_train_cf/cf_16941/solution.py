"""
QUESTION:
Write a function `determine_string_type` that takes a string `input_string` as input and returns its type. The function should return one of the following types based on the input string: "Empty string", "Numeric string", "Alphabetic string", "Alphanumeric string", "Proper noun", "Palindrome", or "Unknown type". The function should not use regular expressions and should have the following time complexities for each condition: O(1) for checking empty string, and O(n) for other conditions where n is the length of the string.
"""

def determine_string_type(input_string):
    if input_string == "":
        return "Empty string"
    elif input_string.isdigit():
        return "Numeric string"
    elif input_string.isalpha():
        if input_string.istitle():
            return "Proper noun"
        return "Alphabetic string"
    elif input_string.isalnum():
        return "Alphanumeric string"
    elif input_string == input_string[::-1]:
        return "Palindrome"
    else:
        return "Unknown type"