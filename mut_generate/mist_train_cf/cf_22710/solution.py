"""
QUESTION:
Write a function `reverse_and_capitalize_words` that takes an array of strings as input, reverses each word, capitalizes them, and returns the result as a comma-separated string. The function should not take any other parameters besides the array of strings.
"""

def reverse_and_capitalize_words(arr):
    reversed_words = [word[::-1].capitalize() for word in arr]
    return ", ".join(reversed_words)