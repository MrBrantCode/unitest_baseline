"""
QUESTION:
Write a function named `max_value` that takes one argument, a list of four numbers. The function should return the maximum value from the list, handling edge cases where all numbers could be negative. The input list must contain exactly four elements, and all elements must be either integers or floats. If the input is not a list or does not meet the length or type requirements, the function should return an error message.
"""

def max_value(arr):
    if len(arr) != 4:
        return "The array length must be 4."
    elif type(arr) != list:
        return "Input must be a list."
    for element in arr:
        if not isinstance(element, (int, float)):
            return "List elements must be numbers."

    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val