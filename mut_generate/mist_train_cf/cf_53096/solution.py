"""
QUESTION:
Write a function `find_multiples(n, start, end)` that returns all multiples of an integer `n` within a range from `start` to `end` (inclusive).
"""

def find_multiples(n, start, end):
    """
    Returns all multiples of an integer n within a range from start to end (inclusive).
    
    Parameters:
    n (int): The integer whose multiples we want to find.
    start (int): The start of the numerical range.
    end (int): The end of the numerical range.
    
    Returns:
    list: A list of multiples of n within the specified range.
    """
    multiples = []
    for i in range(start, end + 1):
        if i % n == 0:
            multiples.append(i)
    return multiples