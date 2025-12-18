"""
QUESTION:
Problem Statement
Given an integer N, find the sum of all primes < N.
Input Format
The only line of the input file contains a positive integer N.

Output Format
Output the sum of all primes < N.

Constraints
1 ≤ N ≤ 4000000
You are guaranteed that the answer will fit in a 64-bit integer.

SAMPLE INPUT
1000

SAMPLE OUTPUT
76127
"""

from math import sqrt

def sum_of_primes_below(N):
    if N <= 2:
        return 0
    
    # Initialize an array to store prime numbers
    arr = [i for i in range(2, N)]
    
    # Apply the Sieve of Eratosthenes
    limit = int(sqrt(N))
    for i in range(2, limit + 1):
        if arr[i - 2] == 0:
            continue
        else:
            incr = i
            num = i * 2
            while num < N:
                arr[num - 2] = 0
                num += incr
    
    # Sum the non-zero elements in the array
    return sum(arr)