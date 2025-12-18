"""
QUESTION:
Create a function named `prime_tuples` that takes a list of integer tuples as input and returns a new list containing only the tuples where all integers are prime numbers.
"""

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_tuples(tuples_list):
    return [t for t in tuples_list if all(is_prime(num) for num in t)]