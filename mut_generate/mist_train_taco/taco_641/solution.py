"""
QUESTION:
You are given an integer n find its next greater or equal number whose binary representation must not contain consecutive ones.

For eg.  given n=6 whose binary is 110 and the next number with no consecutive ones is 8 whose binary is 1000.

INPUT

First line of input contains t, the total number of test cases. Then t line follows n.

0<t<100

0<n<10^5

OUTPUT

The next number on each line.

SAMPLE INPUT
2
6
2

SAMPLE OUTPUT
8
2
"""

def find_next_non_consecutive_ones(n: int) -> int:
    """
    Finds the next greater or equal number to `n` whose binary representation does not contain consecutive ones.

    Parameters:
    n (int): The starting number.

    Returns:
    int: The next number greater than or equal to `n` with no consecutive ones in its binary representation.
    """
    for i in range(n, 100001):
        if "11" not in bin(i):
            return i
    return -1  # In case no such number is found within the given range (should not happen with the problem constraints)