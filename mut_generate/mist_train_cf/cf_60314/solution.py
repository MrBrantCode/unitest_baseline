"""
QUESTION:
Create a function `separates_elements` that takes an array of integers as input and returns two separate arrays. The first array should contain the Fibonacci numbers from the input array in descending order, and the second array should contain the non-Fibonacci numbers in ascending order. If the input array contains non-numeric data, the function should return an error message "Error: Non-numeric data inputs found".
"""

import math

def separates_elements(arr):
    """
    This function separates the Fibonacci numbers from the non-Fibonacci numbers in the input array.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    tuple: A tuple containing two lists. The first list contains the Fibonacci numbers in descending order, 
           and the second list contains the non-Fibonacci numbers in ascending order. If the input array 
           contains non-numeric data, it returns an error message "Error: Non-numeric data inputs found".
    """
    
    # Helper function to check if a number is a Fibonacci number
    def is_fibonacci(n):
        x = 5 * n * n + 4
        y = 5 * n * n - 4
        return math.isqrt(x) ** 2 == x or math.isqrt(y) ** 2 == y

    try:
        fibonacci = sorted([num for num in arr if isinstance(num, int) and is_fibonacci(num)], reverse=True)
        non_fibonacci = sorted([num for num in arr if isinstance(num, int) and not is_fibonacci(num)])
        return fibonacci, non_fibonacci
    except TypeError:
        return "Error: Non-numeric data inputs found"