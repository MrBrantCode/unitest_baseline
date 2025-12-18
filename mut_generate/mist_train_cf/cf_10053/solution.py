"""
QUESTION:
Write a recursive function `recursive_compute_sum` that takes two decimal numbers as strings, converts them to floats, checks if they are within the range of -100 to 100, computes their sum, rounds the result to 2 decimal places, and returns the sum. If the numbers are not within the range or are not valid, the function should display an error message and ask for input again.
"""

def recursive_compute_sum(num1, num2):
    """
    Recursively compute the sum of two decimal numbers as strings, 
    ensuring they are within the range of -100 to 100, 
    and rounds the result to 2 decimal places.

    Args:
    num1 (str): The first decimal number as a string.
    num2 (str): The second decimal number as a string.

    Returns:
    float: The sum of the two decimal numbers rounded to 2 decimal places.
    str: An error message if the numbers are not within the range or are not valid.
    """

    # Convert input numbers to floats
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Invalid input. Please enter valid numbers."

    # Check if numbers are within the specific range
    if num1 < -100 or num1 > 100 or num2 < -100 or num2 > 100:
        return "Numbers must be between -100 and 100"

    # Compute the sum
    sum_result = num1 + num2

    # Round the sum to 2 decimal places
    sum_result = round(sum_result, 2)

    return sum_result