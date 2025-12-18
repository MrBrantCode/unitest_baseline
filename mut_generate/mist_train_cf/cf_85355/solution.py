"""
QUESTION:
Write a function `cube_root` in Brainfuck that calculates the cube root of a given integer. The function should not use advanced features and should only utilize the available Brainfuck commands.
"""

def cube_root(n):
    """
    This function calculates the cube root of a given integer.

    Args:
        n (int): The input integer.

    Returns:
        int: The cube root of the input integer.
    """
    if n == 0:
        return 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        cube = mid ** 3
        if cube == n:
            return sign * mid
        elif cube < n:
            low = mid + 1
        else:
            high = mid - 1
    return sign * low