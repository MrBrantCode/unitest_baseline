"""
QUESTION:
Write a function `double_and_square` that takes a 2D array as input, doubles each item in the array, and then squares each doubled item. The function should return the updated 2D array.
"""

def double_and_square(arr):
    """
    This function doubles each item in a 2D array and then squares each doubled item.

    Args:
        arr (list): A 2D array of numbers.

    Returns:
        list: The updated 2D array with each item doubled and squared.
    """
    # Iterate over each element in the 2D array
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # Double the value and square it
            arr[i][j] = (2 * arr[i][j]) ** 2
    return arr