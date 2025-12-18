"""
QUESTION:
Write a program which reads an integer n and prints the number of prime numbers which are less than or equal to n. A prime number is a natural number which has exactly two distinct natural number divisors: 1 and itself. For example, the first four prime numbers are: 2, 3, 5 and 7.



Input

Input consists of several datasets. Each dataset has an integer n (1 ≤ n ≤ 999,999) in a line.

The number of datasets is less than or equal to 30.

Output

For each dataset, prints the number of prime numbers.

Example

Input

10
3
11


Output

4
2
5
"""

import math

def count_primes_up_to_n(n: int) -> int:
    if n < 2:
        return 0
    
    LIMIT = 1000000
    pList = [True] * (LIMIT + 1)
    pList[0] = pList[1] = False  # 0 and 1 are not prime numbers
    
    p = 2
    while p ** 2 <= LIMIT:
        if pList[p]:
            for i in range(p * 2, LIMIT + 1, p):
                pList[i] = False
        p += 1
    
    count = 0
    for i in range(2, n + 1):
        if pList[i]:
            count += 1
    
    return count