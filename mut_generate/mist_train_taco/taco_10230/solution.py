"""
QUESTION:
Let p (i) be the i-th prime number from the smallest. For example, 7 is the fourth prime number from the smallest, 2, 3, 5, 7, so p (4) = 7.

Given n, the sum of p (i) from i = 1 to n s

s = p (1) + p (2) + .... + p (n)

Create a program that outputs. For example, when n = 9, s = 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 = 100.



Input

Given multiple datasets. Each dataset is given the integer n (n ≤ 10000). When n is 0, it is the last input. The number of datasets does not exceed 50.

Output

For n in each dataset, print s on one line.

Example

Input

2
9
0


Output

5
100
"""

def sum_of_first_n_primes(n: int) -> int:
    if n <= 0:
        return 0
    
    num = 200000
    is_prime = [True] * (num + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(num ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, num + 1, i):
            is_prime[j] = False
    
    primes = [x for x in range(num + 1) if is_prime[x]]
    
    return sum(primes[:n])