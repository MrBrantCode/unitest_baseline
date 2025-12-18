"""
QUESTION:
Write a function `largest_prime_factor(n)` that takes a floating-point number `n` as input, ignores its sign and decimal part, and returns the largest prime factor of the resulting integer. The function should handle cases where `n` is less than or equal to 1, and should be optimized for efficiency by only checking odd factors up to the square root of `n`. The input `n` will have an absolute value greater than 1 and will not be a prime number.
"""

def largest_prime_factor(n: float) -> int:
    n = int(abs(n))  # Ignore the sign and decimal part

    # Corner cases
    if n == 1: return 1

    largest = 2
    while n % 2 == 0:  # Divide by 2 until n is odd
        n = n // 2
    
    # n must be odd at this point, hence skip the even numbers and iterate only for odd
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest = i
            n = n // i
    
    # If n is a prime and larger than 2
    if n > 2: largest = n

    return largest