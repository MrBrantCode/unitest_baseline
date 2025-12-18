"""
QUESTION:
Create a function named `print_prime_and_factorial` that prints all prime numbers between 0 and n (inclusive) along with their corresponding factorial values. The function should be able to handle large numbers efficiently, with n potentially reaching up to 10^9.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
                  
def print_prime_and_factorial(n):
    for number in range(n):
        if is_prime(number):
            print("Prime number: ", number)
            print("Factorial: ", math.factorial(number))