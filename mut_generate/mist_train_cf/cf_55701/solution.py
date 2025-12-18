"""
QUESTION:
Create a function named `monotonic` that takes a list of integers and two parameters, `k` and `strict`, where `k` is an integer representing a fixed interval and `strict` is a boolean indicating whether the sequence must be strictly monotonic. The function should return `True` if every pair of consecutive elements in the list has a difference of `k`, considering the `strict` parameter. If `strict` is `True`, the function should return `False` if any pair of consecutive elements are identical; if `strict` is `False`, the function should allow identical consecutive elements.
"""

def monotonic(lst: list, k: int, strict: bool = False):
    """
    Determine if the sequence of numbers in a list is monotonic, with a constant difference of 'k' between each pair of consecutive elements. If 'strict' is true, the function should return false if any pair of consecutive elements are identical. If 'strict' is false, the sequence can include identical consecutive elements.
    """
    return all(x - y == k or (not strict and x - y == 0) for x, y in zip(lst[1:], lst[:-1]))