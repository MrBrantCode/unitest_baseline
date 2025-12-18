"""
QUESTION:
Create a function named `prime_numbers` that takes two integer arguments, `start` and `end`, and returns a list of all prime numbers between `start` and `end` (inclusive) using a recursive divide-and-conquer strategy. The function should be able to handle cases where `start` is greater than `end`.
"""

def is_prime(n, i = 2):
    # Base case
    if n <= 2:
        if n == 2: 
            return True
        else: 
            return False
    # Base case
    if n % i == 0:
        return False
    if i * i > n:
        return True
    # Check for next divisor
    return is_prime(n, i + 1)

def prime_numbers(start, end):
    # Base case
    if start > end:  
        return []
    else:
        # Recursive case
        if is_prime(start):  
            return [start] + prime_numbers(start + 1, end) 
        else:  
            return prime_numbers(start + 1, end)