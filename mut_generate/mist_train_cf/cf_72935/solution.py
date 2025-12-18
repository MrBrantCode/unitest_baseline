"""
QUESTION:
Write a function named "generateArray" that accepts three integers 'n', 'x', and 'y'. Depending on whether 'n' is a prime number or not, the function should return a list containing either all prime numbers less than 'n' plus the value of 'x', or all non-prime numbers less than 'n' plus the value of 'y'. A prime number is a natural number greater than 1 with no divisors other than 1 and itself.

The function should be declared as `generateArray(int n, int x, int y)`.
"""

def generateArray(n, x, y):
    """
    Returns a list of prime numbers less than 'n' followed by 'x' if 'n' is prime,
    otherwise returns a list of non-prime numbers less than 'n' followed by 'y'.

    Args:
        n (int): The input number to check for primality.
        x (int): The number to append to the list if 'n' is prime.
        y (int): The number to append to the list if 'n' is not prime.

    Returns:
        list: A list of prime or non-prime numbers less than 'n', followed by 'x' or 'y'.
    """

    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Check if 'n' is prime
    if is_prime(n):
        # If 'n' is prime, return a list of prime numbers less than 'n' followed by 'x'
        return [i for i in range(2, n) if is_prime(i)] + [x]
    else:
        # If 'n' is not prime, return a list of non-prime numbers less than 'n' followed by 'y'
        return [i for i in range(1, n) if not is_prime(i)] + [y]