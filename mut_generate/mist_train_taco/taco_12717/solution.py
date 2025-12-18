"""
QUESTION:
The sequence of n - 1 consecutive composite numbers (positive integers that are not prime and not equal to 1) lying between two successive prime numbers p and p + n is called a prime gap of length n. For example, (24, 25, 26, 27, 28) between 23 and 29 is a prime gap of length 6.

Your mission is to write a program to calculate, for a given positive integer k, the length of the prime gap that contains k. For convenience, the length is considered 0 in case no prime gap contains k.



Input

The input is a sequence of lines each of which contains a single positive integer. Each positive integer is greater than 1 and less than or equal to the 100000th prime number, which is 1299709. The end of the input is indicated by a line containing a single zero.

Output

The output should be composed of lines each of which contains a single non-negative integer. It is the length of the prime gap that contains the corresponding positive integer in the input if it is a composite number, or 0 otherwise. No other characters should occur in the output.

Example

Input

10
11
27
2
492170
0


Output

4
0
6
0
114
"""

import math

class Prime:
    def __init__(self, n):
        self.M = m = int(math.sqrt(n)) + 10
        self.A = a = [True] * m
        a[0] = a[1] = False
        self.T = t = []
        for i in range(2, int(math.sqrt(m)) + 1):
            if not a[i]:
                continue
            t.append(i)
            for j in range(i * i, m, i):
                a[j] = False

    def is_prime(self, n):
        return self.A[n]

def calculate_prime_gap_length(k):
    if k <= 1 or k > 1299709:
        return 0
    
    pr = Prime(1299709 ** 2)
    l = r = k
    
    while not pr.is_prime(l):
        l -= 1
    while not pr.is_prime(r):
        r += 1
    
    return r - l