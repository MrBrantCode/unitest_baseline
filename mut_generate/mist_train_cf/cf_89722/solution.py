"""
QUESTION:
Write a function named `sum_prime_numbers` that takes a list of integers as input and returns the sum of the first 3 prime numbers in the list. If the list contains less than 3 prime numbers, the function should return the sum of all prime numbers in the list.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_prime_numbers(lst):
    prime_numbers = []
    for num in lst:
        if is_prime(num):
            prime_numbers.append(num)
            if len(prime_numbers) == 3:
                break
    return sum(prime_numbers)