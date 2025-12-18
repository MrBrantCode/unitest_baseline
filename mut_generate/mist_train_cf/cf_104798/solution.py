"""
QUESTION:
Create a function called `find_primes` that takes an integer `n` as input and returns the list of prime numbers in the range 1-n, the sum of these prime numbers, the average of these prime numbers rounded to two decimal places, the smallest prime number, and the largest prime number.
"""

def find_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = [num for num in range(1, n + 1) if is_prime(num)]
    prime_sum = sum(prime_numbers)
    prime_avg = round(prime_sum / len(prime_numbers), 2) if prime_numbers else 0
    smallest_prime = min(prime_numbers) if prime_numbers else None
    largest_prime = max(prime_numbers) if prime_numbers else None

    return prime_numbers, prime_sum, prime_avg, smallest_prime, largest_prime