"""
QUESTION:
Write a function `find_median()` that takes a set of integers as input, sorts them in ascending order, and returns the median value. The input integers should be passed as a string of space-separated values. The function should handle both even and odd lengths of input integers.
"""

def find_median(num_str):
    """
    This function calculates the median of a set of integers.

    Args:
        num_str (str): A string of space-separated integers.

    Returns:
        float: The median value of the input integers.
    """

    # Convert the input string into a list of integers
    num_list = list(map(int, num_str.split()))

    # Sort the list in ascending order
    num_list.sort()

    n = len(num_list)
    # Check if the length of the list is even or odd
    if n % 2 == 0:
        median = (num_list[n//2 - 1] + num_list[n//2]) / 2
    else:
        median = num_list[n//2]

    return median