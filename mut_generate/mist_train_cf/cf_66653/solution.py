"""
QUESTION:
Write a function `second_largest` that takes a set of numbers as input, identifies the second largest number and its index, and returns them. The function should handle sets with duplicate values and cases where all elements are the same. The function must not use built-in functions for sorting, maximum, or second maximum values. If the set does not have a second largest value, the function should return a message indicating this.
"""

def second_largest(set_values):
    lst = list(set_values)  # Convert set to list
    max_val = second_max_val = float('-inf')  # Initialize maximum and second maximum
    max_index = second_max_index = -1  # Initialize indexes
    for i, num in enumerate(lst):
        if num > max_val:
            second_max_val = max_val
            second_max_index = max_index
            max_val = num
            max_index = i
        elif num != max_val and num > second_max_val:
            second_max_val = num
            second_max_index = i

    if second_max_val == float('-inf'):  # If second maximum doesn't exist
        return "Second largest value doesn't exist"
    return second_max_val, second_max_index  # Return value and index