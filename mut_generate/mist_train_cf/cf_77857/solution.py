"""
QUESTION:
Write a function `count_target` that takes two inputs: an array of integers and a target integer. The function should count the occurrence of the target integer in the array and return -1 if the count equals 0. The function must handle invalid inputs, including non-integer target values and non-integer array elements, and return an error message in such cases.
"""

def count_target(arr, target):
    # Check if arr is a list
    if not isinstance(arr, list):
        return 'Input error: Please provide a list of integers.'

    # Check if target is an integer
    if not isinstance(target, int):
        return 'Input error: Target should be an integer.'

    # Check if all elements in arr are integers
    if not all(isinstance(i, int) for i in arr):
        return 'Input error: Please provide a list of integers.'
    
    count = arr.count(target)

    if count == 0:
        return -1
    else:
        return count