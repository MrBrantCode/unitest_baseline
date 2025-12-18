"""
QUESTION:
Write a function named `calculate_sum(n)` that calculates the sum of the reciprocals of all prime numbers up to and including a given positive integer `n`. The function should take an integer `n` as input and return the sum. Note that the input integer `n` is expected to be a positive integer, and the function should only consider prime numbers in the range from 2 to `n` (inclusive).
"""

def calculate_sum(n):
    """
    Calculates the sum of the reciprocals of all prime numbers up to and including n.
    """
    def check_prime(num):
        """
        Checks if a number is prime.
        """
        if num == 1:
            return False
        elif num == 2:
            return True
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
            
    total = 0
    for i in range(2, n + 1):
        if check_prime(i):
            total += 1/i
    return total