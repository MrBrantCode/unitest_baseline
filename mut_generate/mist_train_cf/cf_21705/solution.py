"""
QUESTION:
Create a function `list_primes(start, end)` that returns a list of all prime numbers between `start` and `end` (inclusive) using only recursive functions to find the prime numbers. If either `start` or `end` is negative, or if `start` is greater than `end`, display a warning message and return an empty list.
"""

def list_primes(start, end):
    if start < 0 or end < 0:
        print("Warning: Both input numbers should be positive.")
        return []
    elif start > end:
        print("Warning: The second number should be greater than the first number.")
        return []
    
    def is_prime(num, divisor=2):
        if num < 2:  
            return False
        elif num == divisor:  
            return True
        elif num % divisor == 0:  
            return False
        else:
            return is_prime(num, divisor + 1)  
    
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    
    return primes