"""
QUESTION:
Write a function `prime_even_sum(array)` that takes a 2D array of integers as input and returns the sum of all even numbers in the array if the sum is a prime number, otherwise returns -1.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_even_sum(array):
    even_sum = sum(num for row in array for num in row if num % 2 == 0)
    return even_sum if is_prime(even_sum) else -1