"""
QUESTION:
Write a function named `print_and_sum_elements` that takes a 3D array as input. The function should print each element of the array along with its corresponding position in the format 'Element X is at position [i][j][k]'. Additionally, the function should return the sum of all elements in the array.
"""

def print_and_sum_elements(arr):
    """
    Prints each element of a 3D array along with its position and returns the sum of all elements.

    Args:
        arr (list): A 3D list of elements.

    Returns:
        int: The sum of all elements in the array.
    """
    total_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(len(arr[i][j])):
                element = arr[i][j][k]
                total_sum += element
                print(f'Element {element} is at position [{i}][{j}][{k}]')
    return total_sum