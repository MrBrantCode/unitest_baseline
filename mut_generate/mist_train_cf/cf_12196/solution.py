"""
QUESTION:
Write a function `findZeros` that takes an array `input` of integers as input and returns a list of indices where the value of the element in the `input` array is 0. The input array is of length n (1 <= n <= 10^6) and the elements are integers between -1000 and 1000.
"""

def find_zeros(input):
    """
    Returns a list of indices where the value of the element in the input array is 0.

    Args:
        input (list): A list of integers.

    Returns:
        list: A list of indices where the value of the element in the input array is 0.
    """
    return [i for i, x in enumerate(input) if x == 0]