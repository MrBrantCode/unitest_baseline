"""
QUESTION:
Write a function called `is_palindrome` that determines whether a given string is a palindrome or not. The function should be case-insensitive, ignore any whitespace characters, punctuation marks, and HTML tags in the string, and handle strings with both uppercase and lowercase letters, numbers, special characters, and non-English characters. It should also handle extremely long strings with a length of up to 10^6 characters and achieve a time complexity of O(n), where n is the length of the input string. Do not use any built-in functions or libraries that directly check for palindromes or reverse strings.
"""

def is_palindrome(s):
    # Remove whitespace and punctuation marks
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Handle HTML tags by removing them
    s = ''.join(char for char in s if char != '<' and char != '>')
    
    # Check if the string is a palindrome
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True