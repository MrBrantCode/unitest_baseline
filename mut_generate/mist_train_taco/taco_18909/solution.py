"""
QUESTION:
Golu loves prime numbers . He wants to do something new with prime numbers. So Molu gives him a number and asks him to minmum number of prime numbers required such that their sum is equal to given number. This task is very diffcult for Golu so he asks you for your help.

Now your task is that you are given a number and you have to find minimum number of prime numbers required such that their sum is equal to given number.

INPUT  First line contains number of test cases T . Each test case contains a single integer N.
OUTPUT  For each test case print in a single line minmum number of primes numbers required. 
Constraints
1 ≤ T ≤ 1000000

2 ≤ N ≤ 1000000 

SAMPLE INPUT
2
2
4

SAMPLE OUTPUT
1
2

Explanation

for N=2 one prime number    (2)

for N=4  two prime numbers (2 + 2)
"""

import math

# Precompute the list of primes up to 1,000,000
primes = []
def primeSieve(sieveSize):
    sieve = [True] * sieveSize
    sieve[0] = False 
    sieve[1] = False
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)

primeSieve(1000000)

def min_primes_for_sum(N):
    if N == 1:
        return 1
    elif N > 2 and N % 2 == 0:
        return 2
    elif N in primes:
        return 1
    elif (N - 2) in primes:
        return 2
    else:
        return 3