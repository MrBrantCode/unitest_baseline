"""
QUESTION:
Create a function `below_threshold_and_prime` that checks if all integers in a given list are below a specified threshold and are prime numbers. The function should return True if all integers meet the conditions and False otherwise. The function should take two parameters: a list of integers and a threshold integer.
"""

def below_threshold_and_prime(lst: list, threshold: int):
    """
    Return True if every integer in list lst is below the threshold and is a prime number.
    """
    def is_prime(n):
        """Check if integer n is a prime"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    for i in lst:
        if i >= threshold or not is_prime(i):
            return False
    return True