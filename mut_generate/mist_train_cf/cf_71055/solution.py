"""
QUESTION:
Write a Python function `move_zeros_to_end` that takes a list as input and returns a new list where all zeroes are moved to the end. The function should maintain the relative order of non-zero elements, handle nested lists by moving their zeroes to the end, and work with multiple data types (integers, floats, strings, and nested lists). Strings containing a '0' should not be moved. The function should not use built-in Python functions to directly solve the problem and should have a time complexity of O(n) or less to efficiently handle large lists with up to 10^6 elements.
"""

def move_zeros_to_end(lst):
    # Base case: if the list is empty, return it as is
    if not lst:
        return lst

    non_zeros = []  # list to hold non-zero elements
    zeros = []  # list to hold zeros
    for i in lst:
        # If an element is a nested list, call the function on it recursively
        if isinstance(i, list):
            non_zeros.append(move_zeros_to_end(i))
        elif i == 0:
            zeros.append(0)
        else:
            non_zeros.append(i)

    return non_zeros + zeros # Return the combined list of non-zeros and zeros with zeros at the end.