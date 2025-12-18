"""
QUESTION:
Define a function `calculate_f` that takes three parameters `x`, `y`, and `z`, and calculates the value of the mathematical function f(x,y,z) = x^n/m + z^y/n, where n is the number of prime numbers between 1-10 and m is the number of prime numbers between 10-20. Use this function to calculate the value of f(2,3,4).
"""

def calculate_f(x, y, z):
    """
    Calculate the value of the mathematical function f(x,y,z) = x^n/m + z^y/n, 
    where n is the number of prime numbers between 1-10 and m is the number of prime numbers between 10-20.

    Args:
        x (int): The base of the first term in the function.
        y (int): The exponent of the second term in the function.
        z (int): The base of the second term in the function.

    Returns:
        float: The value of the function.
    """
    # Define the ranges for prime numbers
    range1 = range(1, 11)
    range2 = range(10, 21)

    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Calculate n and m
    n = sum(1 for num in range1 if is_prime(num))
    m = sum(1 for num in range2 if is_prime(num))

    # Calculate the function value
    return x ** n / m + z ** y / n