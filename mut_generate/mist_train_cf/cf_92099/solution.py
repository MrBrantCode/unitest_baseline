"""
QUESTION:
Write a function named `is_prime()` to check if a given number is prime and use it to calculate the sum of the first N-1 elements of a given list X, where N is the size of the list X. If N is prime, return the sum of the first N-1 elements. If N is not prime, return an error message. The function should take a list X as input and N should be determined from the size of X.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def entrance(X):
    N = len(X)
    if is_prime(N):
        return sum(X[:-1])
    else:
        return "Error: N is not prime."