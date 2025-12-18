"""
QUESTION:
Write a function `remove_duplicates(numbers)` that takes a list of integers as input, removes duplicates and negative numbers, and returns a list of distinct positive integers in descending order.
"""

def remove_duplicates(numbers):
    distinct_numbers = list(set(numbers)) 
    distinct_numbers = [num for num in distinct_numbers if num > 0] 
    distinct_numbers.sort(reverse=True) 
    return distinct_numbers