"""
QUESTION:
Write a function `is_prime(n)` that checks if a number `n` is a prime number. Using this function, generate a list of all prime numbers between 50 and 100. Additionally, compute the average of these prime numbers and find the prime numbers that lie above and below this average. The input range (50, 100) is inclusive of the end point but not the start point.
"""

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True