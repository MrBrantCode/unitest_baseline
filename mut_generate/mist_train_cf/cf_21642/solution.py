"""
QUESTION:
Write a function find_missing_prime(numbers) that finds the smallest missing prime number in a given list of integers, numbers. The list may contain both prime and non-prime numbers, but the missing prime will always be smaller than the largest number in the list.
"""

def find_missing_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_num = max(numbers)
    for i in range(2, max_num + 1):
        if is_prime(i) and i not in numbers:
            return i

    return None