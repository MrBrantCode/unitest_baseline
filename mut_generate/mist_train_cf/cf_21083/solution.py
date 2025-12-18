"""
QUESTION:
Create a function `classify_number` that takes an integer `n` as input where 1 ≤ n ≤ 100. The function should return a string stating whether the number is even or odd and whether it is prime or not prime.
"""

import math

def classify_number(n):
    """
    Classify a number as even or odd and prime or not prime.

    Args:
        n (int): The number to classify.

    Returns:
        str: A string stating whether the number is even or odd and whether it is prime or not prime.
    """
    def is_even(number):
        return number % 2 == 0

    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    even_odd = "even" if is_even(n) else "odd"
    prime_not_prime = "prime" if is_prime(n) else "not prime"

    return f"{n} is {even_odd} and {prime_not_prime}."