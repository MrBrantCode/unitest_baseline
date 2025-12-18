"""
QUESTION:
Write a function `second_highest_element` that takes a list of integers as input and returns the second highest element in the list without using any built-in functions. The function should handle lists with duplicate numbers and return `None` if the list has less than two distinct elements.
"""

def second_highest_element(lst):
    first = float('-inf')
    second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return second if second != float('-inf') else None