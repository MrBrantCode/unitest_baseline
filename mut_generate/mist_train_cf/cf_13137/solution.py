"""
QUESTION:
Write a function `calculate_sum` that takes a list of numbers as input and returns the sum of all numbers in the list. The list may contain nested lists, and the function should recursively sum all numbers within these nested lists.
"""

def calculate_sum(my_list):
    total_sum = 0
    
    for element in my_list:
        if isinstance(element, list):
            total_sum += calculate_sum(element)
        else:
            total_sum += element
    
    return total_sum