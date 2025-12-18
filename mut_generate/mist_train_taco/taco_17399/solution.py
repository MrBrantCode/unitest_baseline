"""
QUESTION:
The chef was busy in solving algebra, he found some interesting results, that there are many numbers which can be formed by sum of some numbers which are prime. Chef wrote those numbers in dairy. Cheffina came and saw what the chef was doing. Cheffina immediately closed chef's dairy and for testing chef's memory, she starts asking numbers and chef needs to answer wheater given number N can be formed by the sum of K prime numbers if it yes then print 1 else print 0. 

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- Each test case contains a single line of input, two integers $N, K$.

-----Output:-----
For each test case, output in a single line answer as 1 or 0.

-----Constraints-----
- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^5$
- $1 \leq K \leq 10^5$

-----Sample Input:-----
2
12 2
11 2

-----Sample Output:-----
1
0
"""

from math import sqrt

def isprime(n):
    if n % 2 == 0 and n > 2 or n == 1:
        return 0
    else:
        s = int(sqrt(n)) + 1
        for i in range(3, s, 2):
            if n % i == 0:
                return 0
        return 1

def can_form_by_prime_sum(N, K):
    if N < 2 * K:
        return 0
    if K == 1:
        return isprime(N)
    if K == 2:
        if N % 2 == 0:
            return 1
        return isprime(N - 2)
    return 1