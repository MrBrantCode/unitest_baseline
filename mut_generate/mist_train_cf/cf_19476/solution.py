"""
QUESTION:
Create a function called `calculate_sum_of_cubes` that takes an array of integers as input. The array must contain at least 5 and at most 10 elements. Each element in the array must be a positive integer between 1 and 100 (inclusive). The function should calculate the sum of the cubes of the elements in the array and return the result as a float rounded to two decimal places if the sum is divisible by both 3 and 5. If any of these requirements are not met, the function should return an error message.
"""

def calculate_sum_of_cubes(arr):
    """
    Calculate the sum of the cubes of elements in the array and return the result as a float rounded to two decimal places 
    if the sum is divisible by both 3 and 5.

    Args:
        arr (list): A list of integers. The list must contain at least 5 and at most 10 elements. 
                    Each element in the list must be a positive integer between 1 and 100 (inclusive).

    Returns:
        float: The sum of the cubes of elements in the array rounded to two decimal places if the sum is divisible by both 3 and 5.
        str: An error message if any of the requirements are not met.
    """

    # Check if the array length is within the required range
    if len(arr) < 5 or len(arr) > 10:
        return "Array length must be between 5 and 10 (inclusive)"

    # Check if the array contains only positive integers between 1 and 100
    for num in arr:
        if not (isinstance(num, int) and num > 0 and num <= 100):
            return "Array elements must be positive integers between 1 and 100"

    # Calculate the sum of the cubes
    sum_of_cubes = sum([num ** 3 for num in arr])

    # Check if the sum is divisible by 3 and 5
    if sum_of_cubes % 3 != 0 or sum_of_cubes % 5 != 0:
        return "Sum of the cubes must be divisible by both 3 and 5"

    # Return the sum of the cubes rounded to two decimal places
    return round(sum_of_cubes, 2)