"""
QUESTION:
Write a function `convert_array_to_string(arr)` that takes an array of 12 integers between -100 and 355 as input, and returns a string where all integers divisible by 5 are excluded. The output string should contain the remaining integers separated by a space.
"""

def convert_array_to_string(arr):
    """
    This function takes an array of 12 integers between -100 and 355, 
    and returns a string where all integers divisible by 5 are excluded.

    Args:
        arr (list): A list of 12 integers between -100 and 355.

    Returns:
        str: A string containing the remaining integers separated by a space.
    """
    result = ""
    for num in arr:
        if num % 5 != 0:
            result += str(num) + " "
    return result.strip()  # Remove trailing whitespace