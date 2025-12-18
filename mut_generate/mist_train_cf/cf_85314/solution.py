"""
QUESTION:
Write a function `mix_candies` to determine the pounds of each candy type Olivia needs to mix together 15 pounds of candies while maintaining a 2:3:1 ratio among the three varieties, given that each variety must be used at least once and she has 5 pounds of the first kind, 6 pounds of the second kind, and 4 pounds of the third kind.
"""

def mix_candies(total_pounds, ratio, available_candies):
    """
    Calculate the pounds of each candy type needed to mix together a given total pounds of candies while maintaining a given ratio.

    Args:
        total_pounds (float): The total pounds of candies.
        ratio (list): A list of integers representing the ratio of each candy type.
        available_candies (list): A list of floats representing the available pounds of each candy type.

    Returns:
        list: A list of floats representing the pounds of each candy type needed.
    """
    total_parts = sum(ratio)
    pounds_per_part = total_pounds / total_parts
    needed_candies = [part * pounds_per_part for part in ratio]
    return needed_candies