"""
QUESTION:
Write a function `get_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The input list may contain duplicate numbers and the function should return the prime numbers in the same order as they appear in the original list.
"""

def get_prime_numbers(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers