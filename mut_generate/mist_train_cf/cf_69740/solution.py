"""
QUESTION:
Write a function named 'find_primes_in_range' to generate a list of prime numbers between two given numbers, 50 and 70. A prime number must be greater than 1 and only divisible by 1 and itself without leaving a remainder. The function should return a list of these prime numbers.
"""

def find_primes_in_range(start, end):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [i for i in range(start, end + 1) if is_prime(i)]