"""
QUESTION:
Develop a function named `largest_prime(n)` that identifies the largest prime divisor for a specified integer `n`. The function should return the largest prime number that divides `n`. The input `n` is a positive integer, and the function should handle cases where `n` itself is a prime number.
"""

def largest_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_divisor = None
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if is_prime(i):
                prime_divisor = i
    if n > 1 and is_prime(n):
        prime_divisor = n
    return prime_divisor