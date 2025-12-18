"""
QUESTION:
Chef Vivek is good in mathematics and likes solving problems on prime numbers. One day his friend Jatin told him about Victory numbers. Victory number can be defined as a number formed after summing up all the prime numbers till given number n. Now, chef Vivek who is very fond of solving questions on prime numbers got busy in some other tasks. Your task is to help him finding victory number.

-----Input:-----
- First line will contain $T$, number of test cases. Then the test cases follow. 
- Each test case contains of a single line of input $N$ till which sum of all prime numbers between 1 to n has to be calculated.

-----Output:-----
For each test case, output in a single line answer to the victory number.

-----Constraints-----
- $1 <= T <= 1000$
- $1 <= N <= 10^6$

-----Sample Input:-----
3
22
13
10

-----Sample Output:-----
77
41
17
"""

from math import sqrt

def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    half = int(sqrt(x)) + 1
    for y in range(3, half, 2):
        if x % y == 0:
            return False
    return True

def calculate_victory_number(n):
    if n == 1:
        return 0
    sum_of_primes = 2 if n >= 2 else 0
    for x in range(3, n + 1, 2):
        if is_prime(x):
            sum_of_primes += x
    return sum_of_primes