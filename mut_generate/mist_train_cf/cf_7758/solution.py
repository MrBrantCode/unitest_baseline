"""
QUESTION:
Create a function `get_prime_numbers` that takes a list of integers as input and returns a list containing only the prime numbers in the input list. The function should have a time complexity of O(n^2), where n is the length of the input list. It should not use any built-in Python functions or libraries for determining prime numbers, and it should include a helper function to check for primality.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_prime_numbers(lst):
    prime_numbers = []
    for num in lst:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers