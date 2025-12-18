"""
QUESTION:
Implement a function `is_palindrome` that determines if a given string is a palindrome or not. The function should ignore case, special characters, and whitespace, and should not use any built-in functions or libraries to check for palindromes. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1), meaning it should only use a constant amount of space. The function should return True if the string is a palindrome and False otherwise.
"""

def is_palindrome(s):
    # Remove special characters and whitespace
    s = ''.join(e for e in s if e.isalnum())
    
    # Convert the string to lowercase
    s = s.lower()

    # Check if the string is a palindrome
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True