"""
QUESTION:
Write a function `is_prime(n)` and use it to calculate the product of all distinct prime numbers in the range 80 to 100. The function should return True if the number is prime and False otherwise. The prime numbers are to be found in the range [80, 100], not including the 100.
"""

def is_prime(n):
    if n == 2 or n == 3: 
        return True
    if n < 2 or n%2 == 0: 
        return False
    if n < 9: 
        return True
    if n%3 == 0: 
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: 
            return False
        if n%(f+2) == 0: 
            return False
        f +=6
    return True    