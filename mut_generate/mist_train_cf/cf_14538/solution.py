"""
QUESTION:
Write a Python function `is_prime_and_calculate` that takes two integers `a` and `b` as input, calculates their sum and product, and returns the sum, product, and a string indicating whether the sum is a prime number. The input integers are restricted to the range 1 <= a, b <= 100.
"""

def is_prime_and_calculate(a, b):
    """
    Calculate the sum and product of two numbers and check if the sum is a prime number.

    Args:
    a (int): The first number.
    b (int): The second number.

    Returns:
    tuple: A tuple containing the sum, product, and a string indicating whether the sum is prime.
    """

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    total = a + b
    product = a * b

    if is_prime(total):
        return total, product, "Prime"
    else:
        return total, product, "Not Prime"