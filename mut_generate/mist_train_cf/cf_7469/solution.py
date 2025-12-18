"""
QUESTION:
Create a function `largest_prime_factor(N1, N2, R)` that finds the largest prime number that is a factor of two numbers `N1` and `N2` and is within the range of 1 to `R`. The function should return -1 if there is no prime factor within the range. Constraints: 1 <= N1, N2 <= 10^9 and 1 <= R <= 10^6.
"""

import math

def largest_prime_factor(N1, N2, R):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    largest_prime = -1
    for i in range(R, 0, -1):
        if N1 % i == 0 and N2 % i == 0 and is_prime(i):
            largest_prime = i
            break
    return largest_prime