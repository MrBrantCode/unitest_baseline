"""
QUESTION:
You are provided with array of positive non-zero ints and int n representing n-th power (n >= 2).

For the given array, calculate the sum of each value to the n-th power. Then subtract the sum of the original array.

Example 1: Input: {1, 2, 3}, 3 --> (1 ^ 3 + 2 ^ 3 + 3 ^ 3 ) - (1 + 2 + 3) --> 36 - 6 --> Output: 30

Example 2: Input: {1, 2}, 5  --> (1 ^ 5 + 2 ^ 5) - (1 + 2) --> 33 - 3 --> Output: 30
"""

def calculate_modified_sum(lst, n):
    """
    Calculate the modified sum of the given list of integers.

    Parameters:
    lst (list of int): A list of positive non-zero integers.
    n (int): The n-th power (n >= 2).

    Returns:
    int: The result of the modified sum calculation.
    """
    sum_of_powers = sum(x ** n for x in lst)
    sum_of_originals = sum(lst)
    return sum_of_powers - sum_of_originals