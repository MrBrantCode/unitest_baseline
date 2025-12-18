"""
QUESTION:
Write a function `is_prime` that prints all prime numbers from 1 to a given number n. The time complexity should not exceed O(n^1.5) and the space complexity should not exceed O(n).
"""

def entance(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True