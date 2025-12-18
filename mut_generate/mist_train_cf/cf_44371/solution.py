"""
QUESTION:
Create a function `tri` that takes a non-negative integer `n` as input and returns a list containing the first `n + 1` numbers of the Tribonacci sequence. The Tribonacci sequence is defined as follows: `tri(0) = 1`, `tri(1) = 3`, `tri(2) = 2`, for even `n`, `tri(n) = 1 + n/2`, and for odd `n`, `tri(n) = tri(n-1) + tri(n-2) + tri(n+1)`.
"""

def tri(n):
    """
    Returns a list containing the first n + 1 numbers of the Tribonacci sequence.

    Args:
    n (int): A non-negative integer.

    Returns:
    list: A list of integers representing the first n + 1 numbers of the Tribonacci sequence.
    """
    result = [0] * (n + 1)

    # Base cases
    result[0] = 1  # By definition we set tri(0) = 1
    if n >= 1:
        result[1] = 3  # By definition we set tri(1) = 3
    if n >= 2:
        result[2] = 2  # By definition we set tri(2) = 2

    # Computation for n > 2
    for i in range(3, n + 1):
        if i % 2 == 0:
            result[i] = 1 + i // 2  # If i is an even number
        else:
            result[i] = result[i - 1] + result[i - 2] + result[i - 3]  # If i is an odd number

    return result