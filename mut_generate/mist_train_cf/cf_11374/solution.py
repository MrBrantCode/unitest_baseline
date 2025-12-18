"""
QUESTION:
Generate a function called `generate_sorted_list` that takes two parameters, `start` and `end`, representing the range of integers to be generated. The function should return a list of integers from `start` to `end` (inclusive) in descending order. The integers can be negative and the range can be large (up to 10^9). The time complexity of the solution should be O(n log n), where n is the number of integers in the range.
"""

def generate_sorted_list(start, end):
    return sorted(range(start, end + 1), reverse=True)