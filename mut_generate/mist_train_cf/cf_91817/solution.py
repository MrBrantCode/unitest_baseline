"""
QUESTION:
Write a function `generate_sorted_list(start, end)` that generates a list of integers between `start` and `end` (inclusive) and returns the list sorted in descending order. The time complexity of the solution should be O(n log n), where n is the number of integers in the range. Note that `start` can be greater than `end` and both values can be negative.
"""

def generate_sorted_list(start, end):
    result = []
    i = start
    while i >= end:
        result.append(i)
        i -= 1
    result.sort(reverse=True)
    return result