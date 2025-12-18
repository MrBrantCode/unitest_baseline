"""
QUESTION:
Create a function called `calculate_sum` that takes a list of integers as input and returns the sum of all elements in the list. The function should not use built-in `sum()` or `reduce()` functions and should have a time complexity of O(n), where n is the length of the input list.
"""

def calculate_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total