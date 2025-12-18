"""
QUESTION:
Create a function named `get_fifth_prime` that takes a list of integers as input and returns the fifth prime number in the list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should assume that there are at least five prime numbers in the input list. The input list is 0-indexed, meaning the first element is at index 0.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_fifth_prime(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers[4]