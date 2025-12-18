"""
QUESTION:
Create three functions in Python: `is_palindrome(n)`, `is_prime(n)`, and `check_number(n)`. 

The function `is_palindrome(n)` should determine if the integer `n` is a palindrome, returning True if it is and False otherwise. The function `is_prime(n)` should determine if the integer `n` is a prime number, returning True if it is and False otherwise. 

The `check_number(n)` function should take an integer `n` as input, use the above functions to check if it is a palindrome and a prime number, and return corresponding messages for each category. 

Optimize the solutions for time and space complexity, considering edge cases.
"""

def is_palindrome(n):
    """ Returns True if n is a palindrome """
    return str(n) == str(n)[::-1]


def is_prime(n):
    """ Returns True if n is a prime number """
    if n <= 1:
        return False
    if n < 4:  #2 and 3 are prime
        return True
    if n % 2 == 0:
        return False
    if n < 9:  #we have already excluded 4,6 and 8.
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6 # All primes greater than 3 can be written in form of 6n ± 1
    return True


def check_number(n):
    """ Checks if the number is a palindrome and a prime """
    if is_palindrome(n):
        print(f"{n} is a palindrome.")
    else:
        print(f"{n} is not a palindrome.")
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")