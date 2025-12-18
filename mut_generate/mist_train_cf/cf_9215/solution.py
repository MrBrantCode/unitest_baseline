"""
QUESTION:
Write a function `generate_tuples` that takes two lists of integers `a` and `b` as input and returns a list of tuples. Each tuple should be a pair of elements, one from `a` and one from `b`, and the sum of the elements in each tuple should be greater than 10.
"""

def generate_tuples(a, b):
    """
    Generate a list of tuples, each containing a pair of elements from lists a and b.
    The sum of the elements in each tuple should be greater than 10.

    Args:
        a (list): The first list of integers.
        b (list): The second list of integers.

    Returns:
        list: A list of tuples, each with a sum greater than 10.
    """
    return [(i, j) for i in a for j in b if i + j > 10]