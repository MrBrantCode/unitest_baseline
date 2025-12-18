"""
QUESTION:
Write a function called `is_palindrome` that determines whether a given string is a palindrome or not. The function should be case-insensitive, ignore whitespace characters and punctuation marks, and handle strings with both uppercase and lowercase letters, whitespace characters, punctuation marks, numbers, special characters, and non-English characters. The function should also handle extremely long strings with a length of up to 10^6 characters and provide a time complexity of O(n), where n is the length of the input string. You are not allowed to use any built-in functions or libraries that directly check for palindromes or reverse strings.
"""

def is_palindrome(string):
    # Preprocess the string by removing whitespace and punctuation marks
    processed_string = ''.join(char.lower() for char in string if char.isalnum())

    # Compare the processed string with its reversed version
    return processed_string == processed_string[::-1]