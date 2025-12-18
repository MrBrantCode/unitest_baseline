"""
QUESTION:
Write a function named `insert_point_descending_primes` that takes two parameters: a value and a sorted list of prime numbers in descending order. The function should check if the given value is a prime number and return an error message if it is not. If the value is prime, the function should locate the right insertion point for the value in the list and return its index.
"""

def is_prime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def insert_point_descending_primes(value, a_list):
    if not is_prime(value):
        return "The value is not a prime number."
    for i in range(len(a_list)):
        if value > a_list[i]:
            return i
    return len(a_list)