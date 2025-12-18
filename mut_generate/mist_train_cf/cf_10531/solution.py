"""
QUESTION:
Create a function called `prime_factorization(num)` that takes an integer `num` as input and returns a list of its prime factors without using any built-in prime factorization functions or libraries. The function should decompose the input number into a list of prime numbers that multiply together to give the original number.
"""

def prime_factorization(num):
    factors = []
    divisor = 2
    
    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num = num / divisor
        else:
            divisor += 1
    
    return factors