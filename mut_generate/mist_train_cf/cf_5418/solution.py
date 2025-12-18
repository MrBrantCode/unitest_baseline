"""
QUESTION:
Create a function named `custom_intersection` that takes two sets of integers as input and returns their intersection. The intersection should only include numbers that are divisible by 3, less than 5, have a prime digit in them (2, 3, 5, 7), and are not multiples of 2 or 5.
"""

def custom_intersection(A, B):
    def has_prime_digit(n):
        prime_digits = set('2357')
        return any(digit in prime_digits for digit in str(n))

    intersection = set(A) & set(B)
    return [num for num in intersection if num % 3 == 0 and num < 5 and has_prime_digit(num) and num % 2 != 0 and num % 5 != 0]