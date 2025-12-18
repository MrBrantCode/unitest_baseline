"""
QUESTION:
Write a function `sum_prime_numbers` that takes a list of integers as input and returns the sum of all prime numbers in the list. If the list contains no prime numbers, the function should return 0. The function should use a single loop and a helper function to check for primality. The time complexity should be O(n), where n is the length of the list.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_prime_numbers(lst):
    prime_sum = 0
    for num in lst:
        if is_prime(num):
            prime_sum += num
    return prime_sum