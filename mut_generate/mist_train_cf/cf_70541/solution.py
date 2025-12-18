"""
QUESTION:
Create a function named `is_palindromic_prime(n)` that takes an integer `n` as input and returns a boolean value indicating whether `n` is a prime number and a palindrome. The function should return `True` if `n` is both prime and palindromic, and `False` otherwise.
"""

def is_palindromic_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        sqrt_num = int(num**0.5) + 1

        for divisor in range(3, sqrt_num, 2):
            if num % divisor == 0:
                return False
        
        return True

    return is_prime(n) and str(n) == str(n)[::-1]