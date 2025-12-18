"""
QUESTION:
Write a function `get_multiples(m, start, end)` that returns a list of all integers within the interval `[start, end]` that are multiples of `m`. The function should take three parameters: `m` (the multiple), `start` (the start of the interval), and `end` (the end of the interval). The interval is inclusive, meaning it includes both `start` and `end`.
"""

def get_multiples(m, start, end):
    return [i for i in range(start, end+1) if i % m == 0]