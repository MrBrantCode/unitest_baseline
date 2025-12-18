"""
QUESTION:
Implement a function `recursive_sum(arr)` that calculates the sum of all elements in a nested list of integers. The function should handle both empty lists and lists containing integers or nested lists of integers. The input list `arr` can contain any level of nesting and may include both positive and negative integers.
"""

def recursive_sum(arr):
    total = 0
    for element in arr:
        if isinstance(element, list):
            total += recursive_sum(element)  # Recursively sum nested lists
        else:
            total += element  # Add integers to the total
    return total