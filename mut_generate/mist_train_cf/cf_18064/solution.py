"""
QUESTION:
Write a function `count_unique_primes` that takes a list of integers as input and returns a dictionary containing the unique prime numbers from the list as keys and their frequencies as values. The function should only include prime numbers in the output and ignore non-prime numbers. The input list can contain duplicate numbers.
"""

def count_unique_primes(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_counts = {}
    for num in arr:
        if is_prime(num):
            if num in prime_counts:
                prime_counts[num] += 1
            else:
                prime_counts[num] = 1

    return prime_counts