"""
QUESTION:
Write a function `find_repeating_pattern` that finds repeating patterns in a given stream of numbers. The function should return the start index and length of the pattern if it appears at least three times; otherwise, return None. The pattern should be as long as possible.
"""

def find_repeating_pattern(stream):
    maxLength = len(stream) // 3  # As pattern should appears at least 3 times
    for length in range(1, maxLength+1):  # Check all lengths from 1 to len/3
        for start in range(0, len(stream) - 2 * length):  # Check all possible start indexes
            pattern = stream[start:start + length]
            if pattern == stream[start + length:start + 2 * length] and pattern == stream[start + 2 * length:start + 3 * length]:
                return (start, length)
    return None  # If no repeating pattern is found