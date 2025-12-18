"""
QUESTION:
n! = n × (n − 1) × (n − 2) × ... × 3 × 2 × 1

Is called the factorial of n. For example, the factorial of 12

12! = 12 x 11 x 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 479001600

And there are two consecutive 0s at the end.

Write a program that inputs the integer n and outputs the number of consecutive 0s at the end of n !. However, n is a positive integer less than or equal to 20000.



Input

Multiple data are given. Each piece of data is given n (n ≤ 20000) on one line. When n is 0, it is the last input.

The number of data does not exceed 20.

Output

For each data, output the number of 0s that are consecutively arranged at the end of n! On one line.

Example

Input

2
12
10000
0


Output

0
2
2499
"""

def count_trailing_zeros_of_factorial(n: int) -> int:
    """
    Counts the number of consecutive zeros at the end of n! (n factorial).

    Parameters:
    n (int): The integer for which the factorial is to be calculated.

    Returns:
    int: The number of consecutive zeros at the end of n!.
    """
    zero_count = 0
    while n:
        n //= 5
        zero_count += n
    return zero_count