"""
QUESTION:
Write a function named `sum_array` that takes an array as input and returns the sum of all numbers within the array, including numbers in nested arrays and objects. The function should handle nested arrays and objects iteratively using a stack data structure, without using recursion.
"""

def sum_array(arr):
    stack = [arr]
    total_sum = 0

    while stack:
        element = stack.pop()

        if isinstance(element, int):
            total_sum += element
        elif isinstance(element, list):
            stack.extend(element)
        elif isinstance(element, dict):
            stack.extend(element.values())

    return total_sum