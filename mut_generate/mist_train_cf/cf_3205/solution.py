"""
QUESTION:
Write a list comprehension function to generate a list of all prime numbers less than 100 that are divisible by 3 and are also palindromic.
"""

def prime_palindromic_divisible_by_3(n):
    return [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5)+1)) and x % 3 == 0 and str(x) == str(x)[::-1]]