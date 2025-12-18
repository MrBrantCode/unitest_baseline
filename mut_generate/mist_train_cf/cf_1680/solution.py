"""
QUESTION:
Implement a function `reverse_print_and_sum` that takes a 2-dimensional array of strings as input. Using a nested for loop, print each string in the array in reverse order. Also, calculate and return the sum of the lengths of all strings in the array. The function should iterate through both the outer and inner arrays in reverse order to print the elements.
"""

def reverse_print_and_sum(array):
    """
    This function takes a 2-dimensional array of strings, prints each string in reverse order, 
    and returns the sum of the lengths of all strings in the array.

    Args:
        array (list): A 2-dimensional array of strings.

    Returns:
        int: The sum of the lengths of all strings in the array.
    """
    total_length = 0
    for i in range(len(array)-1, -1, -1):
        for j in range(len(array[i])-1, -1, -1):
            print(array[i][j])
            total_length += len(array[i][j])
    return total_length