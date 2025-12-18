"""
QUESTION:
Write a function named `find_number_in_2d_array` that takes two parameters: a target integer `num` and a 2D numerical array. The function should return a list of tuples representing the coordinates (i, j) of all occurrences of `num` in the array.
"""

def find_number_in_2d_array(num, array):
    """
    This function takes a target integer and a 2D numerical array as input.
    It returns a list of tuples representing the coordinates (i, j) of all occurrences of the target number in the array.

    Args:
        num (int): The target number to be found in the array.
        array (list): A 2D list of numbers.

    Returns:
        list: A list of tuples, where each tuple contains the coordinates of the target number in the array.
    """
    positions = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == num:
                positions.append((i,j))
    return positions