"""
QUESTION:
Write a function called `sum_of_odd_numbers` that takes a multi-dimensional array of integers as input and returns the sum of all odd numbers in the array. The array can be of any size and have any number of dimensions. The function should not modify the input array.
"""

def sum_of_odd_numbers(arr):
    """
    This function calculates the sum of all odd numbers in a multi-dimensional array.
    
    Args:
        arr (list): A multi-dimensional array of integers.
    
    Returns:
        int: The sum of all odd numbers in the array.
    """
    
    # Initialize sum variable
    total_sum = 0
    
    # Use recursion to flatten the array and calculate the sum
    def recursive_sum(array):
        nonlocal total_sum
        for element in array:
            if isinstance(element, list):
                recursive_sum(element)
            elif element % 2 != 0:
                total_sum += element
    
    # Call the recursive function
    recursive_sum(arr)
    
    return total_sum