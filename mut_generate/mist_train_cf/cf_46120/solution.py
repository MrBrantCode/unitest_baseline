"""
QUESTION:
Write a function `get_prime_numbers(num_list)` that takes a list of distinct integers as input and returns a list of prime numbers from the input list. The function should only consider positive integers greater than 1 as potential prime numbers.
"""

def entrance(num_list):
    primes = [num for num in num_list if num > 1 and all(num%i != 0 for i in range(2, num))]
    return primes