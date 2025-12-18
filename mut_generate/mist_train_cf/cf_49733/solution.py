"""
QUESTION:
Write a function named `check_prime` and a while loop that prints prime numbers within a specified range. The function `check_prime` should take an integer as input and return True if the number is prime, False otherwise. The while loop should start from the number 10 and iterate until it reaches or exceeds 100, incrementing by 4 in each iteration. Ensure that the initial number is within the range [10, 100] and the increment is always 4; if not, print an error message.
"""

def check_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True