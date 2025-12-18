"""
QUESTION:
Implement a function named `second_smallest` that takes a list of integers as input and returns the second smallest element. The function should only use built-in Python functions and not rely on external libraries. The list may contain duplicate values. If the list has less than two unique elements, the function's behavior is undefined.
"""

def second_smallest(numbers):
    smallest = float('inf')
    second_smallest = float('inf')
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest