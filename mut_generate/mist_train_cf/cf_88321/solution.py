"""
QUESTION:
Create a function `prime_descending_array(n)` that takes a positive integer `n` as input and returns an array of size `n` with prime numbers in descending order from `n` to 1. The input integer `n` will be positive and less than or equal to 1000.
"""

def prime_descending_array(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    array = []
    num = n
    while num > 1:
        if is_prime(num):
            array.append(num)
        num -= 1
    return array