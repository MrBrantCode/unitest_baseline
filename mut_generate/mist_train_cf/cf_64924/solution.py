"""
QUESTION:
Write a function `arraySum` that takes an array of integers as input. The function should return an array where each element is the sum of all other elements in the input array except the element at the current index. The function should return an error message if the input is not a list, the list is empty, or if the list contains any non-integer values.
"""

def arraySum(arr):
    if not isinstance(arr, list) or len(arr) == 0:
        return "Error: input should be a non-empty list"
    for i in arr:
        if not isinstance(i, int):
            return "Error: all elements in the list should be integers"
    return [sum(arr) - i for i in arr]