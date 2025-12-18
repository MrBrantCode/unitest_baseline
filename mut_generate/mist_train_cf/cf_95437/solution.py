"""
QUESTION:
Write a function named `count_element` that takes a multi-dimensional matrix and a target element as input, and returns the count of the target element in the matrix. The matrix can contain nested lists. Implement the function using recursion with at least two base cases. The function should be able to handle a matrix of any size and any level of nesting.
"""

def count_element(matrix, target):
    # Base case 1: Empty matrix, count is zero
    if len(matrix) == 0:
        return 0

    count = 0
    for element in matrix:
        # Base case 2: Element found, increment count
        if element == target:
            count += 1

        # Recursive case: If element is a nested matrix, call the function recursively
        if isinstance(element, list):
            count += count_element(element, target)

    return count