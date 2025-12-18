"""
QUESTION:
Create a function called `reorder_array` that takes an array of integers as input and returns a reordered array where all even elements come before odd elements. The original order of even and odd elements within their respective groups should be preserved.
"""

def reorder_array(arr):
    """Reorders a given array such that all even elements are placed before odd elements."""
    even = [i for i in arr if i % 2 == 0]
    odd = [j for j in arr if j % 2 != 0]

    return even + odd