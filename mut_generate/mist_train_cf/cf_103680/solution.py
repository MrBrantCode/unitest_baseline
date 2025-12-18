"""
QUESTION:
Write a function named `myfunc` that takes an integer `n` as input and returns the total number of times both `i` and `j` are even numbers in all possible pairs of integers `i` and `j` ranging from 0 to `n-1`. The function must iterate over all pairs of integers in the given range and count the pairs where both `i` and `j` are even.
"""

def myfunc(n):
    """
    This function calculates the total number of times both i and j are even numbers 
    in all possible pairs of integers i and j ranging from 0 to n-1.

    Args:
    n (int): The upper limit of the range.

    Returns:
    int: The total number of pairs where both i and j are even.
    """
    count = 0
    for i in range(n):
        for j in range(n):
            if i % 2 == 0 and j % 2 == 0:
                count += 1
    return count