"""
QUESTION:
Develop a function named `multiply_list` that takes a list of integers as input and returns the product of all integers in the list. The list is not empty and contains only numeric values. The function should initialize a variable to 1 and then multiply each number in the list with this variable.
"""

def multiply_list(items):
    total = 1
    for num in items:
        total *= num
    return total