"""
QUESTION:
Create a function called `row_sums` that takes a two-dimensional array as input and returns a list containing the sum of each row. However, the function should only include positive numbers in the calculation and ignore any negative numbers. The function should handle arrays with varying row lengths.
"""

def row_sums(arr):
    """
    This function calculates the sum of each row in a two-dimensional array, 
    considering only positive numbers.

    Parameters:
    arr (list): A two-dimensional array of integers.

    Returns:
    list: A list containing the sum of each row.
    """
    return [sum([num for num in row if num >= 0]) for row in arr]