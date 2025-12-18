"""
QUESTION:
Write a recursive function `find_largest_prime(n, divisor=2)` to calculate the largest prime factor of a given number `n`. The function should start with the smallest prime number as the divisor and continually divide `n` by the divisor whenever `n` is divisible by the divisor, incrementing the divisor until `n` is no longer divisible. The function should return the largest prime factor when `n` equals the divisor.
"""

def find_largest_prime(n, divisor=2):
    # base case, n is a prime number
    if n == divisor:
        return n
    # n is divisible by divisor
    elif n % divisor == 0:
        return find_largest_prime(n//divisor, divisor)
    # increment divisor and try again
    else:
        return find_largest_prime(n, divisor+1)