"""
QUESTION:
Implement a function `get_unique_elements` that takes a list of integers as its argument and returns a new list containing only the unique elements from the original list, preserving their original order. The function should not use any built-in Python data structures or libraries.
"""

def get_unique_elements(input_list):
    unique_elements = []
    for num in input_list:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements