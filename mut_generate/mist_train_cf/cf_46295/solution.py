"""
QUESTION:
Inheritances are to be divided among two offspring, with one portion exceeding the other by 25%. Write a function called `divide_inheritance` that calculates the amount each child will inherit given the total wealth. The total wealth is $600,000.
"""

def divide_inheritance(total_wealth):
    """
    Calculate the amount each child will inherit given the total wealth.

    One portion exceeds the other by 25%. This function returns a tuple where
    the first element is the smaller portion and the second element is the larger portion.

    Args:
        total_wealth (float): The total wealth to be divided.

    Returns:
        tuple: A tuple of two floats representing the smaller and larger portions.
    """
    smaller_portion = total_wealth / 2.25
    larger_portion = 1.25 * smaller_portion
    return smaller_portion, larger_portion