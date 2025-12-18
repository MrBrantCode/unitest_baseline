"""
QUESTION:
Write a function `print_2d_array` that prints all the elements of a given 2D array in row-wise order, without using any loops or recursion. The input is a 2D list of integers, and the output should be a string where all elements are separated by a space.
"""

def print_2d_array(arr):
    """
    Prints all the elements of a given 2D array in row-wise order without using any loops or recursion.

    Args:
        arr (list): A 2D list of integers.

    Returns:
        str: A string where all elements are separated by a space.
    """
    # Flatten the 2D array using list comprehension
    flattened_arr = [str(num) for sublist in arr for num in sublist]

    # Return the flattened array in row-wise order using join()
    return " ".join(flattened_arr)