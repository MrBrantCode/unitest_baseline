"""
QUESTION:
Create a function named `geometric_mean` that takes a list of integers as input and returns the integer in the list closest to the geometric mean of the list. The list must contain only positive integers. If the input list is invalid, return an error message. In case of a tie for the closest number, return the smallest of these numbers.
"""

def geometric_mean(lst):
    """
    Calculate the integer in the list closest to the geometric mean.

    Args:
    lst (list): A list of positive integers.

    Returns:
    int: The integer in the list closest to the geometric mean. If the input list is invalid, return an error message.
    """

    # Check that all elements of lst are positive integers
    # If not, return an error message
    for i in lst:
        if not isinstance(i, int) or i <= 0:
            return "Error: All elements of list must be positive integers"

    # Calculate the geometric mean
    product = 1
    for i in lst:
        product *= i
    gm = product ** (1.0/len(lst))

    # Find the element of lst closest to the geometric mean
    # If there is a tie, return the smallest number
    closest = None
    smallest_diff = None
    for i in lst:
        diff = abs(gm - i)
        if smallest_diff is None or diff < smallest_diff or (diff == smallest_diff and i < closest):
            closest = i
            smallest_diff = diff

    return closest