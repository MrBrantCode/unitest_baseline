"""
QUESTION:
Write a function `is_prime(n)` that checks if a number `n` is prime and use it to print all prime numbers between 1 and a given number. The function should return `False` if the number is not prime and the loop to print prime numbers should iterate from 1 to 10.
"""

def entrance(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True