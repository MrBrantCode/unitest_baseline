"""
QUESTION:
Create a function `advanced_prime_factors_conditions(n, m)` that takes two positive integers `n` and `m` as input and returns the total number of `n`-digit positive integers that meet the following conditions:

* The number starts or ends with 1 or `m`.
* The number is divisible by more than three distinct prime numbers.
* The sum of the digits of the number is even.
* The product of the first and last digits of the number is even.

Note that the function should be efficient but may have a relatively high time complexity due to the prime check and factorization processes.
"""

import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.sqrt(n)
    for i in range(3, int(sqrt_n) + 1, 2):
        if n % i == 0:
            return False
    return True

# Function to get factors of a number
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return list(set(factors))

def advanced_prime_factors_conditions(n, m):
    start = 10 ** (n - 1)
    end = 10 ** n
    count = 0
    for num in range(start, end):
        str_num = str(num)
        if str_num[0] in ['1', str(m)] or str_num[-1] in ['1', str(m)]:
            if sum(int(x) for x in str_num) % 2 == 0:
                if (int(str_num[0]) * int(str_num[-1])) % 2 == 0:
                    factors = prime_factors(num)
                    if len(factors) > 3 and all(is_prime(fact) for fact in factors):
                        count += 1
    return count