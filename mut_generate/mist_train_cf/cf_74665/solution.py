"""
QUESTION:
Write a function named `reconfigure_array` that takes an array of integers as input, and returns a new array where all prime numbers are positioned on the left and non-prime numbers are on the right. The function should maintain the relative order of prime and non-prime numbers within their respective groups. The function should not contain any main or test code, and should not take any additional parameters.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def reconfigure_array(array):
    prime_numbers = [num for num in array if is_prime(num)]
    non_prime_numbers = [num for num in array if not is_prime(num)]
    return prime_numbers + non_prime_numbers