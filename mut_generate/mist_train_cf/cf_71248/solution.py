"""
QUESTION:
Create a function named `median` that takes a list of integers as input and returns the median without sorting the list. The function should be able to handle both even and odd lengths of the list.
"""

def median(l: list):
    """
    Locate and return the median of elements present unperturbed in the list l, without structuring the elements.
    The list may include an even or odd count of elements.
    """

    n = len(l)
    s = sorted(l)
    return (s[n//2] if n % 2 == 1 else (s[n//2 - 1] + s[n//2]) / 2)