"""
QUESTION:
Implement a function named `reverse_string` that takes a string `s` as input and returns the reversed string. The function should handle edge cases where the input string is empty or `None`. Note that strings in Python are immutable and cannot be changed in-place. The solution should use integer division (`//`) to avoid truncation errors.
"""

def reverse_string(s):
    if not s:
        return s
    s = list(s)
    for i in range(len(s) // 2):
        temp = s[i]
        s[i] = s[len(s) - i - 1]
        s[len(s) - i - 1] = temp
    return ''.join(s)