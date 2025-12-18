"""
QUESTION:
Write a function named `count_unique_primes` that takes an array of integers as input, and returns a dictionary with unique prime numbers as keys and their frequencies as values, along with the sum of these prime numbers.
"""

def count_unique_primes(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_counts = {}
    prime_sum = 0
    for num in arr:
        if is_prime(num):
            if num in prime_counts:
                prime_counts[num] += 1
            else:
                prime_counts[num] = 1
            prime_sum += num
    return prime_counts, prime_sum