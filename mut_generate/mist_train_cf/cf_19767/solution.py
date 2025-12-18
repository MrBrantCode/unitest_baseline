"""
QUESTION:
Write a function named `find_second_largest` that takes an array of numbers as input and returns the second largest number in the array without using built-in sorting or max functions. If there is no second largest number (i.e., all numbers are the same), the function should handle this case accordingly.
"""

def find_second_largest(arr):
    """
    This function finds the second largest number in an array without using built-in sorting or max functions.
    
    Parameters:
    arr (list): A list of numbers.
    
    Returns:
    int: The second largest number in the array. If there's no second largest number, it returns the largest number.
    """
    largest = arr[0]
    second_largest = arr[0]
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
            
    return second_largest