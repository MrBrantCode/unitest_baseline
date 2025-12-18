"""
QUESTION:
Create a function `sum_first_n_primes` that calculates the sum of the first n prime numbers. The input is the number of prime numbers, and the output is the sum of these numbers. The input should be a positive integer.
"""

def sum_first_n_primes(n):
    def is_prime(num):
        """Check if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    """Calculate the sum of the first n prime numbers"""
    prime_sum = 0
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            prime_sum += num
            count += 1
        num += 1
    return prime_sum