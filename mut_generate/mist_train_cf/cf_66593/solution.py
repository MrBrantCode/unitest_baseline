"""
QUESTION:
Create a function `prime_less_than(n)` that takes a positive integer `n` as input and returns a list of all prime numbers less than `n`. The function should not include `n` in the output. The input `n` is a positive integer.
"""

def prime_less_than(n):
    def is_prime(num):
        """Check if a number is prime or not"""
        if num < 2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes