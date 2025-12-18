"""
QUESTION:
Create a function called `prime_range` that checks whether a given number falls within a specified range of prime numbers. The function should take three parameters: `start`, `end`, and `num`. It should return `True` if `num` is within the range `[start, end]` and is a prime number, and `False` otherwise. Assume `start` and `end` are inclusive.
"""

def prime_range(start, end, num):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    return num >= start and num <= end and is_prime(num)