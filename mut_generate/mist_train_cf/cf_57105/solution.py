"""
QUESTION:
Create a function `fibonacci_product` that takes three parameters: an integer `M`, an integer `P`, and a boolean flag. The function should calculate and return the product of all Fibonacci sequence numbers between 0 and `M` (inclusive) that are greater than `P`. If the boolean flag is `True`, only consider Fibonacci numbers that are prime. The function should be optimized to handle large values of `M`.
"""

def fibonacci_product(M, P, boolean_flag):
    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n%2 == 0:
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n%i == 0:
                return False    
        return True

    a, b = 0, 1
    product = 1
    while a <= M:
        if a > P and (not boolean_flag or is_prime(a)):
            product *= a
        a, b = b, a+b
    return product