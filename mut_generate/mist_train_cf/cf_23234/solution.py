"""
QUESTION:
Write a function named `reverse_and_filter_primes` that takes a list of integers as input, reverses the list, and returns a new list containing only the prime numbers from the reversed list.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def reverse_and_filter_primes(numbers):
    reversed_list = list(numbers[::-1])
    prime_numbers = [num for num in reversed_list if is_prime(num)]
    return prime_numbers