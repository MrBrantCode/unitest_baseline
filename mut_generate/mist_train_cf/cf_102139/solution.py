"""
QUESTION:
Create a function called `count_even_numbers` that takes a list of integers as input and returns the count of even numbers in the list. If the input is an empty list or None, the function should return -1. The function must have a time complexity of O(n) and a space complexity of O(1). Zero is considered an even number.
"""

def count_even_numbers(lst):
    if lst is None or len(lst) == 0:
        return -1
    
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    
    return count