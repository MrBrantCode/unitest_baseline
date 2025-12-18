"""
QUESTION:
Create a function `is_prime` to check if a number is prime and use it in a loop to print all prime numbers between 1 and 1000. The function should take an integer as input and return a boolean indicating whether the number is prime. The loop should print each prime number on a new line.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True