"""
QUESTION:
A prime number is an integer that is greater than 1 and can only be divided by itself or 1. For example, 2 is a prime number because it is divisible only by 2 and 1, but 12 is not a prime number because it is divisible by 2, 3, 4, 6 in addition to 12 and 1.

When you enter the integer n, write a program that outputs the largest prime number less than n and the smallest prime number greater than n.



Input

Given multiple datasets. Each dataset is given n (3 ≤ n ≤ 50,000) on one row.

The number of datasets does not exceed 50.

Output

For each dataset, output the largest prime number less than n and the smallest prime number greater than n on one line, separated by a space.

Example

Input

19
3517


Output

17 23
3511 3527
"""

from math import sqrt, ceil

def find_prime_neighbors(n):
    N = 53000
    temp = [True] * (N + 1)
    temp[0] = temp[1] = False
    
    for i in range(2, ceil(sqrt(N + 1))):
        if temp[i]:
            temp[i + i::i] = [False] * len(temp[i + i::i])
    
    largest_prime_less_than_n = n - 1 - temp[n - 1:0:-1].index(True)
    smallest_prime_greater_than_n = n + 1 + temp[n + 1:].index(True)
    
    return largest_prime_less_than_n, smallest_prime_greater_than_n