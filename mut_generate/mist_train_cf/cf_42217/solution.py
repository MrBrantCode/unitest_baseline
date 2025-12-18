"""
QUESTION:
Create a function named `is_prime` that takes an integer `num` as input and returns a boolean value indicating whether the input number is prime or not. The function should return `True` if the input number is prime and `False` otherwise. Do not use any external libraries or built-in functions to check for prime numbers. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def entrance(num: int) -> bool:
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):  
            if (num % i) == 0:
                return False  
        return True  
    else:
        return False 