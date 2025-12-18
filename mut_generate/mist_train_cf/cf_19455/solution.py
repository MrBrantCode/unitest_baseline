"""
QUESTION:
Write a function `is_isogram(s)` that determines if a given string `s` is an isogram. The function should consider both uppercase and lowercase letters and ignore special characters and spaces. It should have a time complexity of O(n), where n is the length of the input string, and should not use any additional data structures.
"""

def is_isogram(s):
    checker = 0
    s = s.lower()
    for ch in s:
        diff = ord(ch) - ord('a')
        if diff < 0 or diff > 25:
            continue
        if (checker & (1 << diff)) != 0:
            return False
        checker |= (1 << diff)
    return True