"""
QUESTION:
Create a function `create_dictionary(x, y)` that takes two parameters: a prime number `x` greater than 1,000,000 and a prime number `y` greater than 100,000. The function should return a dictionary where each key is a unique prime number congruent to 3 modulo 4 within the range from `x` to `y` (inclusive), and the value of each key is the product of `x` and `y`.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def create_dictionary(x, y):
    dictionary = {}
    for num in range(x, y + 1):
        if is_prime(num) and num % 4 == 3:
            product = x * y
            dictionary[num] = product
    return dictionary