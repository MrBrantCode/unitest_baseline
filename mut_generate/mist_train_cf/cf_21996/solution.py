"""
QUESTION:
Create a function named `find_largest_prime_factor` that takes three integers `N1`, `N2`, and `R` as input and returns the largest prime number that is a factor of both `N1` and `N2` within the range of 1 to `R`. If no prime factor is found within the range, the function should return -1.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_largest_prime_factor(N1, N2, R):
    largest_prime_factor = -1
    for i in range(1, R+1):
        if N1 % i == 0 and N2 % i == 0 and is_prime(i):
            largest_prime_factor = max(largest_prime_factor, i)
    return largest_prime_factor