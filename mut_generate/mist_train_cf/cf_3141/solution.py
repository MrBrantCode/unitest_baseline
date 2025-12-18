"""
QUESTION:
Create a function `is_prime(num)` that takes an integer `num` as input and returns `True` if the number is prime and `False` otherwise. Use this function in the main program to count the number of prime numbers in a list of up to 10000 items, where each item is a positive integer between 1 and 1000, and calculate the product of all the prime numbers in the list.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True