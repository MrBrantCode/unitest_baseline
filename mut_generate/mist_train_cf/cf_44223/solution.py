"""
QUESTION:
Create a function `extract_color` that takes an n-tuple of colors and a positive integer k as input, and returns the k-th to the last item from the tuple. If k is out of bound, the function should return an exception message.
"""

def extract_color(color_tuple, k):
    """
    Extracts the k-th to the last item from a tuple of colors.

    Args:
        color_tuple (tuple): A tuple of colors.
        k (int): A positive integer.

    Returns:
        The k-th to the last color in the tuple, or an error message if k is out of bound.
    """
    try:
        return color_tuple[-k]
    except IndexError:
        return "Error: k is out of bound."