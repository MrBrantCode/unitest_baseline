"""
QUESTION:
Write a function `find_primes(a, b)` that takes two non-negative integers `a` and `b` as input, where `b` is greater than `a`, and returns a list of all prime numbers between `a` and `b` (inclusive).
"""

def find_primes(a, b):
    """
    This function takes two non-negative integers a and b as input, 
    where b is greater than a, and returns a list of all prime numbers 
    between a and b (inclusive).
    
    Parameters:
    a (int): The lower limit (inclusive)
    b (int): The upper limit (inclusive)
    
    Returns:
    list: A list of all prime numbers between a and b (inclusive)
    """
    def is_prime(n):
        """Check if a number is prime"""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [num for num in range(a, b+1) if is_prime(num)]