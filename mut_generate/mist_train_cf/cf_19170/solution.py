"""
QUESTION:
Create a function find_pair_of_indices(A, B) that takes two arrays A and B of the same length as input and returns True if there exists a pair of indices (i, j) such that A[i] is a prime number and B[j] is a Fibonacci number, otherwise False.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    return ((5 * n**2 + 4) ** 0.5).is_integer() or ((5 * n**2 - 4) ** 0.5).is_integer()

def find_pair_of_indices(A, B):
    for i in range(len(A)):
        if is_prime(A[i]):
            for j in range(len(B)):
                if is_fibonacci(B[j]):
                    return True
    return False