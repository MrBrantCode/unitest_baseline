"""
QUESTION:
Implement a function named `reverse_string` that takes a string `s` as input and returns its reversed version. The function should not use any built-in string reversal functions or methods. The time complexity of the solution must be O(n log n).
"""

def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        mid = len(s) // 2
        left_half = reverse_string(s[:mid])
        right_half = reverse_string(s[mid:])
        return right_half + left_half