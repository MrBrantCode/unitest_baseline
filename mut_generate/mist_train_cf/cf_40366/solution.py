"""
QUESTION:
Write a function `longest_consecutive_ones(s: str) -> int` that takes a string of binary digits as input and returns the count of the longest consecutive sequence of 1s in the string.
"""

def longest_consecutive_ones(s: str) -> int:
    max_count = 0
    current_count = 0

    for char in s:
        if char == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count