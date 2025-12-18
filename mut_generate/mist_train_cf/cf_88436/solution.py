"""
QUESTION:
Implement a function named `reverse_array` that takes an array of elements as input, creates a clone of the array, reverses the order of the cloned array's elements using recursion, and returns the reversed array without modifying the original array. Do not use any built-in array manipulation functions such as `reverse` or `slice`.
"""

def reverse_array(arr):
    if len(arr) == 0:
        return []
    else:
        return [arr[-1]] + reverse_array(arr[:-1])