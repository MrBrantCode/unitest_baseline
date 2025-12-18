"""
QUESTION:
Write a function named `sum_of_primes` that accepts a multi-dimensional array of integers as input and returns the sum of all prime numbers in the array. The function should use recursion to parse through the nested arrays.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n ** 0.5) + 1
    for divisor in range(3, sqrt_n, 2):
        if n % divisor == 0:
            return False
    return True

def sum_of_primes(arr):
    sum_ = 0
    for element in arr:
        if type(element) is list:
            sum_ += sum_of_primes(element)  
        elif is_prime(element):
            sum_ += element
    return sum_