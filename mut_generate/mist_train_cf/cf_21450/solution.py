"""
QUESTION:
Write a function `is_prime` to determine whether a given integer `n` is a prime number or not. The function must use an iterative solution, constant space complexity (i.e., no additional data structures besides a few variables), and a time complexity of O(sqrt(n)). Do not use any built-in functions or libraries for mathematical operations.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True