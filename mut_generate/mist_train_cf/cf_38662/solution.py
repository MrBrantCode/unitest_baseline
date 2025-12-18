"""
QUESTION:
Write a function `longest_consecutive_zeros` that takes a string `s` consisting only of '0's and '1's as input and returns the length of the longest consecutive sequence of '0's in the string. The function should return an integer value representing the length of the longest sequence.
"""

def longest_consecutive_zeros(s: str) -> int:
    max_zeros = 0
    current_zeros = 0
    for c in s:
        if c == '0':
            current_zeros += 1
            max_zeros = max(max_zeros, current_zeros)
        else:
            current_zeros = 0
    return max_zeros