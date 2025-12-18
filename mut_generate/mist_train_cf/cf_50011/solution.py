"""
QUESTION:
Write a function `find_multiples(num, start, end)` that takes three integers as arguments and returns a list of multiples of `num` that lie within the range of `start` to `end` (inclusive). The function should return all numbers between `start` and `end` that are divisible by `num`.
"""

def find_multiples(num, start, end):
    """
    Returns a list of multiples of `num` within the range of `start` to `end` (inclusive).
    
    Args:
        num (int): The number for which multiples are to be found.
        start (int): The start of the range.
        end (int): The end of the range.
    
    Returns:
        list: A list of multiples of `num` within the specified range.
    """
    return [i for i in range(start, end + 1) if i % num == 0]