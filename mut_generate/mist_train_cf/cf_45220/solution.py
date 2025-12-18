"""
QUESTION:
Write a function `sum_product_subarrays(arr)` that calculates the sum of the products of all possible subarrays within the given list `arr`. The function should be efficient to handle extensive lists and capable of processing lists containing integers, floating point numbers, negative numbers, recurring numbers, and zeros. The function should not use any external libraries or modules and should return the result rounded to 4 decimal places.
"""

def sum_product_subarrays(arr):
    """
    Calculate the sum of the products of all possible subarrays within the given list.

    Args:
        arr (list): A list of numbers.

    Returns:
        float: The sum of the products of all possible subarrays, rounded to 4 decimal places.
    """
    summation = 0
    for i in range(len(arr)):
        product = 1
        for j in range(i, len(arr)):
            product *= arr[j]
            summation += product
    return round(summation, 4)