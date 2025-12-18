"""
QUESTION:
Implement a function `find_minimum` that takes an array of elements as input and returns the minimum element in the array. The function should use recursion, have a time complexity of O(n^2), and not use any built-in sorting or searching functions, arithmetic or bitwise operations, control flow statements, helper functions, or external libraries. The function should also use only constant space and be written in a single line of code.
"""

def find_minimum(arr):
    return arr[0] if len(arr) == 1 else find_minimum(arr[1:]) if arr[0] > arr[1] else find_minimum([arr[0]] + arr[2:])