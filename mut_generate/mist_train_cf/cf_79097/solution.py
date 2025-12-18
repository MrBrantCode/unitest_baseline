"""
QUESTION:
Determine the aggregate of all positive integers n that do not surpass 100,000,000 for which, for every factor d of n, the equation d + n / d results in a prime number. The function should be named `aggregate`.
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def aggregate():
    """
    Calculate the sum of all numbers n that do not surpass 100,000,000 
    for which, for every factor d of n, the equation d + n / d results in a prime number.

    Returns:
    int: The sum of all such numbers.
    """
    summation = 0
    n = 1
    while n <= 100000000:
        if is_prime(n + 1) and is_prime(n // 2 + 2):
            summation += n
        n *= 2
    return summation