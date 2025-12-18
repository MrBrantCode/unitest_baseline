"""
QUESTION:
Write a function called `isPalindrome` that checks if a given string is a palindrome or not. The function should consider only alphanumeric characters and ignore cases. It should not use any additional data structures and have a time complexity of O(n) or better.
"""

def isPalindrome(s: str) -> bool:
    s = ''.join(c.lower() for c in s if c.isalnum())  # Keep lowercase alphanumeric characters
    n = len(s)

    # Checking if the given string is a palindrome
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False

    return True