"""
QUESTION:
Write a function `compare_primes(A, B)` that compares two numbers A and B and returns "A is greater than B" if A is greater than B and both A and B are prime numbers within the range of 1 to 1000. The function should return None if either A or B is not a prime number within the specified range.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def compare_primes(A, B):
    """
    Compare two numbers A and B and return "A is greater than B" if A is greater than B 
    and both A and B are prime numbers within the range of 1 to 1000.
    
    Args:
        A (int): The first number.
        B (int): The second number.
    
    Returns:
        str or None: "A is greater than B" if A is greater than B and both A and B are prime numbers, 
                     otherwise None.
    """
    if 1 <= A <= 1000 and is_prime(A) and 1 <= B <= 1000 and is_prime(B) and A > B:
        return "A is greater than B"
    else:
        return None