"""
QUESTION:
Write a function named `sum_array` that takes an array `arr` as input. The function should add all numbers in the array and return the sum. The array may contain nested arrays or objects, and the function should handle these cases by iterating through all nested elements. The function must use a stack data structure to process the elements iteratively, without using recursion.
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