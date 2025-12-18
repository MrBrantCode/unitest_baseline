"""
QUESTION:
Write a function `second_largest(numbers)` that takes a list of integers as input, and returns the second largest distinct number in the list. If there is no second largest distinct number (i.e., the list is empty, contains only one distinct number, or all numbers are the same), return -1.
"""

def entrance(numbers):
    distinct_numbers = sorted(set(numbers), reverse=True)
    
    if len(distinct_numbers) < 2:
        return -1
    
    return distinct_numbers[1]