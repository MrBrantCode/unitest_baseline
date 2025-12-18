"""
QUESTION:
Given integer n, find length of n! (which is factorial of n) excluding trailing zeros.

Input

The first line of the standard input contains one integer t (t<10001) which is the number of test cases.

In each of the next t lines there is number n (0 ≤ n ≤ 5*10^9).

Output

For each test, print the length of n! (which is factorial of n).

Constraints

1 ≤ t ≤ 10
1 ≤ n ≤ 10^9

SAMPLE INPUT
3
5
7
10

SAMPLE OUTPUT
2
3
5
"""

from math import ceil, log, lgamma

def calculate_factorial_length_excluding_trailing_zeros(n):
    def trailing_zeros(x):
        fives = 0
        i = 1
        while 5**i <= x:
            fives += x // (5**i)
            i += 1
        return fives
    
    if n == 0:
        return 1  # 0! is 1, which has a length of 1
    
    factorial_length = int(ceil(lgamma(n + 1) / log(10)))
    trailing_zero_count = trailing_zeros(n)
    
    return factorial_length - trailing_zero_count