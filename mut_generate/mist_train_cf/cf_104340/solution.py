"""
QUESTION:
Create a function named "is_prime" that takes an integer as input and returns True if the number is prime, and False otherwise. The function should handle the special case where the number is less than 2 and check divisibility up to the square root of the input number. Use this function within a loop to print all the prime numbers between 1 and 1000 (including 1 and 1000).
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True