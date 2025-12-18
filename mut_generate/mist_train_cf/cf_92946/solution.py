"""
QUESTION:
Create a function `get_odd_numbers(start, end)` that returns an array of all odd numbers between `start` and `end` (inclusive), including negative numbers. Ensure `start` is less than or equal to `end`; otherwise, return an empty array.
"""

def get_odd_numbers(start, end):
    if start > end:
        return []
    
    odd_numbers = [num for num in range(start, end + 1) if num % 2 != 0]
    
    return odd_numbers