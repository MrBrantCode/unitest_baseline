"""
QUESTION:
Write a function called `is_palindromic_prime(n)` that checks if a given integer `n` is both a prime number and a palindromic number. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself, and a palindromic number is a number that remains the same when its digits are reversed. Assume that the input `n` is a valid integer.
"""

def is_palindromic_prime(n): 
    def is_prime(num): 
        if num < 2: 
            return False
        for i in range(2, int(num**0.5) + 1): 
            if num % i == 0: 
                return False
        return True
  
    def is_palindromic(num): 
        return str(num) == str(num)[::-1] 
  
    return is_prime(n) and is_palindromic(n)