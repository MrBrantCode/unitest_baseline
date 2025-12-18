"""
QUESTION:
Write a function called `calculate_sum` that takes a list of integers as input and returns the sum of all the elements in the list. The function should initialize a variable `result` to 0 and iterate over each element `curr` in the input list, accumulating the sum in the `result` variable.
"""

def calculate_sum(arr):
    result = 0
    for curr in arr:
        result += curr
    return result