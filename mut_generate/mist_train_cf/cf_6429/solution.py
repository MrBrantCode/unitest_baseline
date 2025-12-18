"""
QUESTION:
Write a function `is_prime(n)` and use it in a list comprehension to generate a list of cubes of all prime numbers between 1 and 1,000,000. The solution must have a time complexity of O(n√n), where n is the upper limit of the range (1,000,000). The function should not use any external libraries or built-in functions to check for prime numbers and should not use any additional memory except for the resulting list of cubes.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True