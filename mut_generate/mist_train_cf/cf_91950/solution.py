"""
QUESTION:
Write a function `find_max(lst)` that takes a list of integers as input and returns the maximum integer in the list without using any built-in functions or methods to find the maximum value. The list may contain negative numbers, and the function should handle this case correctly.
"""

def find_max(lst):
    max_value = float('-inf')  

    for num in lst:
        if num > max_value:
            max_value = num

    return max_value