"""
QUESTION:
Create a function `prime_composite_numbers(arr)` that takes an array of integers as input and returns a quadruple `(x, y, z, w)` where `x` is the smallest non-negative prime integer, `y` is the most significant negative prime integer, `z` is the least non-negative composite integer, and `w` is the most significant negative composite integer. If a digit does not satisfy these specifications, return `None`.
"""

def prime_composite_numbers(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_composite(num):
        if num < 4: 
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False

    min_positive_prime = None
    max_negative_prime = None
    min_positive_composite = None
    max_negative_composite = None

    for value in arr:
        if value > 0 and is_prime(value):
            if min_positive_prime is None:
                min_positive_prime = value
            elif value < min_positive_prime:
                min_positive_prime = value

        elif value < 0 and is_prime(abs(value)):
            if max_negative_prime is None:
                max_negative_prime = value
            elif value > max_negative_prime:
                max_negative_prime = value

        elif value > 0 and is_composite(value):
            if min_positive_composite is None:
                min_positive_composite = value
            elif value < min_positive_composite:
                min_positive_composite = value 

        elif value < 0 and is_composite(abs(value)):
            if max_negative_composite is None:
                max_negative_composite = value
            elif value > max_negative_composite:
                max_negative_composite = value 

    return min_positive_prime, max_negative_prime, min_positive_composite, max_negative_composite