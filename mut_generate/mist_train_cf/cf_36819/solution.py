"""
QUESTION:
Calculate the result of `(integer / 2) + 1` for each integer in a list and output the results. The input list will contain `n` integers, where `1 ≤ n ≤ 100` and `-10^9 ≤ integer ≤ 10^9`. The function should take the list of integers as input and return the results as output.
"""

def calculate_result(lst):
    """
    Calculate the result of (integer / 2) + 1 for each integer in a list and return the results.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A list of results.
    """
    return [(integer // 2 + 1) for integer in lst]