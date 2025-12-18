"""
QUESTION:
Given N numbers A[i], find the count of prime numbers.

Input Specifications:

The first line contains number of Test cases, T.
For each test case T,
    The first line contains N.
    N lines follow with A[1] to A[n]

Output Specifications

For every test case T, a count of the total number of prime numbers

Hint: 0 and 1 are not prime numbers

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 1000000
0 ≤ A[i] ≤ 1000
Register for IndiaHacksSAMPLE INPUT
1
5
45 
31
7
28
90

SAMPLE OUTPUT
2

Register for IndiaHacks
"""

import math

def check_prime(no):
    if no == 0 or no == 1:
        return False
    start = 2
    end = int(math.sqrt(no))
    while start <= end:
        if no % start == 0:
            return False
        start += 1
    return True

def count_prime_numbers(test_cases):
    results = []
    for case in test_cases:
        prime_count = sum(1 for num in case if check_prime(num))
        results.append(prime_count)
    return results