"""
QUESTION:
The chef won a duet singing award at Techsurge & Mridang 2012. From that time he is obsessed with the number 2.

He just started calculating the powers of two. And adding the digits of the results.

But he got puzzled after a few calculations. So gave you the job to generate the solutions to 2^n and find their sum of digits.

-----Input-----
N : number of inputs N<=100

then N lines with input T<=2000

-----Output-----
The output for the corresponding input T

-----Example-----
Input:
3
5
10
4

Output:
5
7
7

Explanation:
2^5=32
3+2=5
2^10=1024
1+0+2+4=7
2^4=16
1+6=7
"""

from operator import add
from functools import reduce

def calculate_power_of_two_digit_sum(T: int) -> int:
    """
    Calculate the sum of the digits of 2^T.

    Parameters:
    T (int): The exponent for which we need to calculate 2^T and then find the sum of its digits.

    Returns:
    int: The sum of the digits of 2^T.
    """
    num_str = list(map(int, str(2 ** T)))
    suma = reduce(add, num_str)
    return suma