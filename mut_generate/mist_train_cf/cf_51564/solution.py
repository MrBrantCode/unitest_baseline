"""
QUESTION:
Write a function `sum_array(arr)` that calculates the cumulative sum of all numerical elements in a given array, handling both integers and floating-point numbers, with a time complexity of O(n) and space complexity of O(1).
"""

def sum_array(arr):
    total = 0.0
    for element in arr:
        if isinstance(element, (int, float)):
            total += element
    return total