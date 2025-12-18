"""
QUESTION:
Write a function `calculate_total_prime_numbers(numbers)` that calculates the total of all prime numbers in a given list `numbers`. The list `numbers` may contain up to 100 elements. The function should return the sum of all prime numbers in the list.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_total_prime_numbers(numbers):
    total = 0
    for num in numbers:
        if is_prime(num):
            total += num
    return total