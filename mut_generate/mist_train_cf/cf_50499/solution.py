"""
QUESTION:
Write a function `count_odd_perfect_squares` that takes two integers `lower_limit` and `upper_limit` as input and returns the quantity of odd perfect square numbers between `lower_limit` and `upper_limit` (inclusive). The function should consider only perfect squares whose values fall within the given range and are odd.
"""

import math

def count_odd_perfect_squares(lower_limit, upper_limit):
    """
    Returns the quantity of odd perfect square numbers between lower_limit and upper_limit (inclusive).

    Args:
        lower_limit (int): The lower limit of the range (inclusive).
        upper_limit (int): The upper limit of the range (inclusive).

    Returns:
        int: The quantity of odd perfect square numbers between lower_limit and upper_limit.
    """

    # find the square roots of the bounds
    lower_sq_root = math.ceil(math.sqrt(lower_limit)) 
    upper_sq_root = math.floor(math.sqrt(upper_limit)) 

    # set initial count to zero
    count = 0

    # iterate through the range
    for i in range(lower_sq_root, upper_sq_root + 1):
        # calculate the square of the number
        square = i * i
        # check if the square is odd
        if square % 2 != 0:
            # increment the count
            count += 1

    return count