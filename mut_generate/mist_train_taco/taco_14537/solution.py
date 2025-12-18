"""
QUESTION:
In this Kata, you're to complete the function `sum_square_even_root_odd`.

You will be given a list of numbers, `nums`, as the only argument to the function. Take each number in the list and *square* it if it is even, or *square root* the number if it is odd. Take this new list and find the *sum*, rounding to two decimal places.

The list will never be empty and will only contain values that are greater than or equal to zero.

Good luck!
"""

def sum_square_even_root_odd(nums):
    """
    Transforms each number in the list by squaring it if it is even, or taking the square root if it is odd.
    Returns the sum of these transformed numbers, rounded to two decimal places.

    Parameters:
    nums (list of int or float): A list of numbers to be transformed and summed.

    Returns:
    float: The sum of the transformed numbers, rounded to two decimal places.
    """
    return round(sum((n ** 2 if n % 2 == 0 else n ** 0.5 for n in nums)), 2)