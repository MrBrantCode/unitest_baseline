"""
QUESTION:
Create a function `prime_numbers_in_range(a, b)` that displays all prime numbers between a given range `a` and `b` (inclusive). The function should take two integers `a` and `b` as input, where `a` and `b` are the start and end of the range respectively.
"""

def prime_numbers_in_range(a, b):
    """
    Displays all prime numbers between a given range.
    """
    def is_prime(num):
        """
        Checks if a number is prime or not.
        """
        if num == 1:
            return False
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False 
        return True

    for num in range(a, b+1):
        if is_prime(num):
            print(num,' is prime.')