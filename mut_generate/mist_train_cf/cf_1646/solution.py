"""
QUESTION:
Write a function named `is_prime` that checks if a given number is prime and use it in a while loop. The loop should start from the smallest prime number greater than or equal to 10 and continue as long as the number is prime and less than or equal to 1000. The function and loop should be able to handle any integer input.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True