"""
QUESTION:
Write a function `get_prime_numbers` that takes a list of integers as input and returns a list of prime numbers in descending order without duplicates. The function should not use any built-in sorting or duplicate removal functions.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_numbers(numbers):
    prime_set = set(x for x in numbers if is_prime(x))
    prime_list = list(prime_set)
    for i in range(len(prime_list)):
        for j in range(i + 1, len(prime_list)):
            if prime_list[i] < prime_list[j]:
                prime_list[i], prime_list[j] = prime_list[j], prime_list[i]
    return prime_list