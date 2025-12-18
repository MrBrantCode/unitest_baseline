"""
QUESTION:
Write a function `delete_largest_prime` that takes a list of integers as input, finds the largest prime number in the list, removes all occurrences of it, and returns the modified list. The function should handle cases where the input list is empty or contains no prime numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def delete_largest_prime(numbers):
    largest_prime = None
    for num in numbers:
        if is_prime(num):
            if largest_prime is None or num > largest_prime:
                largest_prime = num
    if largest_prime is not None:
        numbers = [num for num in numbers if num != largest_prime]
    return numbers