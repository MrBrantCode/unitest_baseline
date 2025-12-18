"""
QUESTION:
Create a function called `count_even_numbers` that takes a list of integers as input and returns the count of even numbers in the list. If the input list is empty or None, the function should return -1. The input list can contain both positive and negative integers, and zero is considered an even number.
"""

def count_even_numbers(lst):
    if lst is None or len(lst) == 0:
        return -1
    
    return sum(1 for num in lst if num % 2 == 0)