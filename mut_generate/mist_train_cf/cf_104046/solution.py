"""
QUESTION:
Write a function called `find_second_largest` that takes a list of numbers as input and returns the second largest value in the list. You are not allowed to use any built-in sorting functions or libraries. If the list has less than two distinct numbers, the function should still return a value, but the actual return value is not specified.
"""

def find_second_largest(lst):
    max_val = float('-inf')
    second_max_val = float('-inf')
    
    for num in lst:
        if num > max_val:
            second_max_val = max_val
            max_val = num
        elif num > second_max_val and num != max_val:
            second_max_val = num
    
    return second_max_val