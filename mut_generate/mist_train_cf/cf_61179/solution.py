"""
QUESTION:
Write a function `isPalindrome(s: str, ignoredChars: str) -> bool` that determines if string `s` is a palindrome considering only alphanumeric characters and ignoring cases, as well as any characters found in `ignoredChars`. The function should return `True` if `s` is a palindrome and `False` otherwise. The function must have a time complexity of O(n) where n is the length of `s`, and a space complexity of O(1). The input strings `s` and `ignoredChars` consist only of printable ASCII characters, and `1 <= s.length <= 2 * 10^5`.
"""

def isPalindrome(s: str, ignoredChars: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while (left < right) and (not s[left].isalnum() or s[left] in ignoredChars):
            left += 1
        while (left < right) and (not s[right].isalnum() or s[right] in ignoredChars):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True