"""
QUESTION:
Create a function named `check_prime` and a for-loop that iterates over a given list of integers and breaks upon encountering a prime number. The function `check_prime(num)` should take an integer `num` as input and return `True` if the number is prime, and `False` otherwise. The loop should print the first prime number it encounters and then terminate.
"""

def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False