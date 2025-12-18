"""
QUESTION:
Create a function `get_sum(x, y)` that calculates the sum of all integers from `min(x, y)` to `max(x, y)` inclusive. The function should be efficient and easy to understand, with a time complexity of O(1).
"""

def get_sum(x, y):
    m = max(x, y)
    n = min(x, y)
    return int(((m * (m + 1)) - ((n - 1) * n)) / 2)