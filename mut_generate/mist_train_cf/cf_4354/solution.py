"""
QUESTION:
Implement the `is_prime` function to efficiently determine whether a given number is prime or not. The function should have a time complexity of O(sqrt(n)) and space complexity of O(1).
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True