"""
QUESTION:
Create a function called `get_odd_numbers` that takes two parameters `start` and `end` and returns an array of all odd numbers between `start` and `end` (inclusive). The function should handle negative numbers and ensure that `start` is less than or equal to `end`. If `start` is greater than `end`, the function should return an empty array.
"""

def get_odd_numbers(start, end):
    if start > end:
        return []
    
    odd_numbers = []
    current_number = start
    
    while current_number <= end:
        if current_number % 2 != 0:
            odd_numbers.append(current_number)
        current_number += 1
    
    return odd_numbers