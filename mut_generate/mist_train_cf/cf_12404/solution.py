"""
QUESTION:
Create a function `is_prime(num)` that takes an integer as input and returns a boolean indicating whether the number is prime or not. The function should be used to filter prime numbers from a given array of integers. The input array may contain numbers up to 17. The function should be efficient and handle numbers up to the square root of the input number.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True