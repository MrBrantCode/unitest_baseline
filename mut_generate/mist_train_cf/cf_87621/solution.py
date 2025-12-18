"""
QUESTION:
Write a function to find the sum of all prime numbers from 1 to n (excluding multiples of 3 or 5). The function should iterate through the numbers from 1 to n, check if a number is prime and not a multiple of 3 or 5, and keep track of the sum of the valid numbers.
"""

def sum_of_primes_excluding_multiples(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum(num for num in range(1, n) if num % 3 != 0 and num % 5 != 0 and is_prime(num))