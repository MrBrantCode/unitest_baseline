"""
QUESTION:
Write a function named `sum_even` that takes a list of integers as input, returns the sum of all even numbers in the list that are not divisible by 3 or 5 and not prime numbers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_even(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(num for num in lst if num % 2 == 0 and num % 3 != 0 and num % 5 != 0 and not is_prime(num))