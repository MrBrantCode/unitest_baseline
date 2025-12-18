"""
QUESTION:
Write a function named `cumulative_sum` that calculates the cumulative sum of the numbers which are multiples of the numbers in the `multiples` list, going up to the `limit` number. The function should accept two arguments: `limit` (an integer) and `multiples` (a list of integers). The `multiples` list can only contain multiples of 3 and 5 between 3 and 15 (inclusive). The function should also handle invalid user inputs by raising a ValueError if the numbers in the `multiples` list are not multiples of 3 or 5, or if they are outside the specified range.
"""

def cumulative_sum(limit, multiples):
    try:
        result = sum(i for i in range(limit + 1) if any(i % m == 0 for m in multiples))
        return result
    except Exception as e:
        return str(e)