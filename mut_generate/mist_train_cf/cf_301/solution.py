"""
QUESTION:
Write a function named `is_prime` to check if a number is prime and use it to calculate the sum of all prime numbers between 1 and 1000 using a for loop. The function should take one integer as input and return a boolean value indicating whether the number is prime or not. The numbers in the range are inclusive of 1 but exclusive of 1000.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True