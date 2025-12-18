"""
QUESTION:
Write a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. Then use this function to calculate the sum of the squares of all prime numbers up to and including a given positive integer `num` input by the user. The function should handle the case where the input number is not a positive integer by printing an error message.
"""

def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n>2 and n%2==0:
        return False
    max_div = int(n**0.5)
    for i in range(3, max_div+1, 2):
        if n%i==0:
            return False
    return True