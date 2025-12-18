"""
QUESTION:
Problem

Let $ f (x) $ be the sum of each digit when the non-negative integer $ x $ is expressed in binary.
Given a positive integer $ N $, output the largest of $ f (0) $, $ f (1) $, ..., $ f (N) $.


Example of calculating the function $ f (5) $:
When 5 is expressed in binary, it is 101 and the sum of each digit is 1 + 0 + 1 = 2
Therefore, $ f (5) = 2 $.


Note: https://ja.wikipedia.org/wiki/ Binary

Ouput

Outputs the largest of $ f (0) $, $ f (1) $, ..., $ f (N) $ on one line.

Constraints

The input satisfies the following conditions.

* $ 1 \ le N \ le 10 ^ 9 $

Input

The input is given in the following format.


$ N $


A positive integer $ N $ is given on one line.

Examples

Input

2


Output

1


Input

9


Output

3
"""

def max_binary_digit_sum(N: int) -> int:
    """
    Calculate the largest sum of binary digits for all integers from 0 to N.

    Parameters:
    N (int): A positive integer.

    Returns:
    int: The largest sum of binary digits for any integer from 0 to N.
    """
    def binary_digit_sum(x: int) -> int:
        """Helper function to calculate the sum of binary digits of a given integer."""
        return bin(x).count('1')
    
    max_sum = 0
    for i in range(N + 1):
        max_sum = max(max_sum, binary_digit_sum(i))
    
    return max_sum