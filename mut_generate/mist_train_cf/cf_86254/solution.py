"""
QUESTION:
Create a function `isPalindrome` that takes a string `s` as input and returns a boolean indicating whether the string is a palindrome, ignoring non-alphanumeric characters and considering alphanumeric characters case-insensitively. The function should handle strings with a length of up to 10^18 characters, different character encodings and multibyte characters, including Unicode characters, and use a constant amount of additional memory, regardless of the input string length. The time complexity of the function should be O(n), where n is the length of the input string.
"""

def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left <= right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    
    return True