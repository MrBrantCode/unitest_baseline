"""
QUESTION:
Create a function named `is_prime` that takes an integer `num` as input and returns `True` if the number is prime and `False` otherwise, using a systematic process that checks divisibility up to the square root of the number. The function should handle invalid inputs (non-positive integers) and return `False` for them.
"""

def is_prime(num):
    # Check for invalid input 
    if num <= 1: 
        return False

    # 2 and 3 are prime 
    if num <= 3:
        return True
    
    # Check divisibility by 2 and 3
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i * i <= num:
        # Check divisibility by factors 
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True