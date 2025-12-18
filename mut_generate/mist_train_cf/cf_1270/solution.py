"""
QUESTION:
Write a function `convert_array_to_string` that takes an array of integers as input. The function should convert the array into a string where each number is separated by a space. However, any integer that is divisible by 5 and not divisible by 3 should be excluded from the final string. The integers in the array are between -100 and 355.
"""

def convert_array_to_string(arr):
    """
    Converts an array of integers into a string where each number is separated by a space.
    Any integer that is divisible by 5 and not divisible by 3 is excluded from the final string.

    Args:
        arr (list): An array of integers between -100 and 355.

    Returns:
        str: A string representation of the array with the specified conditions applied.
    """
    result = ""
    for num in arr:
        if num % 5 == 0 and num % 3 != 0:
            continue
        result += str(num) + " "
    return result.strip()