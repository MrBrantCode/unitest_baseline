"""
QUESTION:
Write a function `min_stamps` that takes a list of distinct positive integer stamp values and a positive integer total mailing cost, and returns the minimum number of stamps needed to achieve the total mailing cost. The function should assume that the stamp values can be combined to achieve the total mailing cost and that the total mailing cost is an integer.
"""

def min_stamps(stamps, total):
    """
    This function calculates the minimum number of stamps needed to achieve a total mailing cost.

    Args:
    stamps (list): A list of distinct positive integer stamp values.
    total (int): A positive integer total mailing cost.

    Returns:
    int: The minimum number of stamps needed.
    """
    stamps.sort(reverse=True)
    num_stamps = 0

    for stamp in stamps:
        while total >= stamp:
            total -= stamp
            num_stamps += 1

    return num_stamps