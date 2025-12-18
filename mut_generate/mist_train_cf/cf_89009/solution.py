"""
QUESTION:
Create a function called `find_sum` that takes an array of positive integers as input. The function should return the sum of all numbers in the array that are divisible by 3, have a remainder of 1 when divided by 4, are greater than 10, and have at least two distinct prime factors.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_sum(numbers):
    sum = 0
    for num in numbers:
        if num % 3 == 0 and num % 4 == 1 and num > 10:
            prime_factors = set()
            for i in range(2, num):
                if num % i == 0 and is_prime(i):
                    prime_factors.add(i)
            if len(prime_factors) >= 2:
                sum += num
    return sum