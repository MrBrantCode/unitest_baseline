"""
QUESTION:
Write a function `sum_array_recursive` that takes a 2D array and returns the sum of its elements as a hexadecimal number. The function should use recursion to calculate the sum and have a time complexity of O(n), where n is the total number of elements in the array. The function should also handle cases where the array is empty, contains non-integer elements, or is not a valid 2D array.
"""

def sum_array_recursive(array):
    """
    Recursive function to calculate the sum of the elements in the array and return it as a hexadecimal number.
    
    Args:
        array (list): A 2D list of integers.
    
    Returns:
        str: The sum of the elements in the array as a hexadecimal number.
    """
    def recursive_sum(array, i, j):
        if i >= len(array):
            return 0
        if j >= len(array[i]):
            return recursive_sum(array, i + 1, 0)
        return array[i][j] + recursive_sum(array, i, j + 1)

    total_sum = recursive_sum(array, 0, 0)
    return hex(total_sum)