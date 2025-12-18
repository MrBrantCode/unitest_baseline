"""
QUESTION:
Write a function `is_prime(num)` to check if a number is prime and use it to find the first prime number greater than 50 from the given list of numbers. The function should return the first prime number greater than 50. Note that the function should only iterate through the numbers in the given list.
"""

def entrance(num):
    for i in range(51, num + 1):
        if is_prime(i):
            return i

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True