"""
QUESTION:
Write a function named `get_prime_numbers` that takes a list of integers as input and returns a new list containing all the prime numbers from the original list. The function should not use any built-in prime number calculation functions or libraries and should implement the primality test manually. The time complexity of the function should be O(n * sqrt(m)), where n is the length of the input list and m is the largest number in the list.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_numbers(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes