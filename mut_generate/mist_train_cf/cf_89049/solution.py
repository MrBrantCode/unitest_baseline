"""
QUESTION:
Write a recursive function `is_palindrome_recursive` that determines if an input string `s` is a palindrome, considering both uppercase and lowercase letters and ignoring any non-alphabetic characters. The function must have a time complexity of O(n), where n is the length of the input string, and it cannot use any built-in string manipulation functions or data structures, or any loops.
"""

def is_palindrome_recursive(s):
    def is_alphabetic(char):
        return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

    def check_palindrome(left, right):
        if left >= right:
            return True

        while left < right and not is_alphabetic(s[left]):
            left += 1

        while left < right and not is_alphabetic(s[right]):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        return check_palindrome(left + 1, right - 1)

    return check_palindrome(0, len(s) - 1)