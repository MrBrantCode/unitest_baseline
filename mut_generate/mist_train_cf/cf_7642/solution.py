"""
QUESTION:
Write a function `is_prime(n)` to check if a number is prime, then use this function to print all prime numbers from 1 to 100 along with their factors on the same line, separated by commas. The time complexity should not exceed O(n^1.5) and the space complexity should not exceed O(n).
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True