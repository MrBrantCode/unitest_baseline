"""
QUESTION:
Write a function `find_multiples(n, start, end)` that finds all multiples of `n` within the interval from `start` to `end` (inclusive). The function should return a list of integers representing the multiples of `n` in the given range.
"""

def find_multiples(n, start, end):
    result = []
    for i in range(start, end+1):
        if i%n == 0:
            result.append(i)
    return result