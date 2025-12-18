"""
QUESTION:
The problem is quite simple. You're  given a number N and a positive integer K. Tell if N can be represented as a sum of K prime numbers (not necessarily distinct).

Input Format 

The first line contains a single integer T, denoting the number of test cases. 

Each of the next T lines contains two positive integers, N & K, separated by a single space.  

Output Format 

For every test case, output "Yes" or "No" (without quotes).

Constraints 

1 <= T <= 5000 

1 <= N <= 10^{12} 

1 <= K <= 10^{12}    

Sample Input

2
10 2
1 6

Sample Output

Yes
No

Explanation  

In the first case, 10 can be written as 5 + 5, and 5 is a prime number.
In the second case, 1 cannot be represented as a sum of prime numbers, because there are no prime numbers less than 1.
"""

import random

def is_probable_prime(n, k=7):
    if n < 6:
        return [False, False, True, True, False, True][n]
    if n & 1 == 0:
        return False
    (s, d) = (0, n - 1)
    while d & 1 == 0:
        (s, d) = (s + 1, d >> 1)
    for a in random.sample(range(2, n - 2), min(n - 4, k)):
        x = pow(a, d, n)
        if x != 1 and x + 1 != n:
            for r in range(1, s):
                x = pow(x, 2, n)
                if x == 1:
                    return False
                elif x == n - 1:
                    a = 0
                    break
            if a:
                return False
    return True

def can_be_sum_of_k_primes(n, k):
    if n < 2 * k:
        return False
    if k == 1:
        return is_probable_prime(n)
    if k == 2:
        if n % 2 == 0:
            return True
        else:
            return is_probable_prime(n - 2)
    return True