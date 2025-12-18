"""
QUESTION:
Create a function named find_median that takes an array of decimal numbers as input and returns the median of the array. The array can be of any size and may contain positive, negative, or zero numbers. The function should handle both odd and even length arrays and return the median as a decimal number.
"""

def find_median(array):
    """
    This function calculates the median of a given array of decimal numbers.
    
    Parameters:
    array (list): A list of decimal numbers.
    
    Returns:
    float: The median of the array.
    """
    # Sort the array in ascending order
    array.sort()

    # Find the length of the array
    n = len(array)

    # Check if the length is odd or even
    if n % 2 == 0:
        # If even, calculate the average of the two middle elements
        median = (array[n//2] + array[n//2 - 1]) / 2
    else:
        # If odd, the median is the middle element
        median = array[n//2]

    return median