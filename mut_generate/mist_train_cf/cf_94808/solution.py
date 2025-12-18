"""
QUESTION:
Write a function `is_prime` that takes an integer as input and returns True if the number is prime and False otherwise. Then, use this function to create a list of all prime numbers between 1 and 100 (inclusive), calculate the sum and product of these prime numbers, and output the list of prime numbers, their sum, and their product. The function should be efficient enough to handle numbers up to 100.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True