"""
QUESTION:
Write a function named `is_palindrome` that checks if a given input string is a palindrome, ignoring any punctuation marks and spaces, and being case-insensitive. The function should return a boolean value indicating whether the input string is a palindrome or not.
"""

import string

def is_palindrome(input_str):
    # Remove punctuation marks and spaces from the input string
    input_str = input_str.translate(str.maketrans("", "", string.punctuation + " "))

    # Convert the input string to lowercase
    input_str = input_str.lower()

    # Check if the reversed input string is equal to the original input string
    return input_str == input_str[::-1]