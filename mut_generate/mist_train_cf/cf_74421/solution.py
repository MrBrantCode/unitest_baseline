"""
QUESTION:
Create a function named `process_nums` that takes a list of integers as input, and returns a new list where each element from the input list is tripled, excluding any prime numbers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def process_nums(lst):
    result = [n*3 for n in lst if not is_prime(n)]
    return result