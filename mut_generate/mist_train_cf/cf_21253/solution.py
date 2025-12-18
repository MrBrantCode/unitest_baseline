"""
QUESTION:
Write a recursive function `A(n)` that takes a positive integer `n`, decreases it by 3 in each recursive call, and terminates when `n` becomes negative. The function should have a time complexity of O(n) and space complexity of O(1), be tail-recursive, and not use any additional data structures.
"""

def A(n):
    """
    This function implements a recursive algorithm with a time complexity of O(n) and space complexity of O(1).
    It decreases the input number by 3 in each recursive call and terminates when the number becomes negative.

    Args:
        n (int): A positive integer.

    Returns:
        int: The result of the recursive algorithm.
    """
    if n < 0:
        return 0
    else:
        return A(n - 3)