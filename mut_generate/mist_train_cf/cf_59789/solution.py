"""
QUESTION:
Write a recursive function `sum_elements_recursive` that calculates the sum of all elements in a list. The function should take two parameters: the list of numbers and an optional index (default 0) to keep track of the current position in the list. The function should not use loops or built-in sum functions.
"""

def sum_elements_recursive(list1, index=0):
    if index == len(list1):
        return 0
    return list1[index] + sum_elements_recursive(list1, index + 1)