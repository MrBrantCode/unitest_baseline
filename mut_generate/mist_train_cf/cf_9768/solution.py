"""
QUESTION:
Create a function called `largest_prime` that takes a list of positive integers as input and returns the largest prime number in the list. If no prime number is found, the function should return -1. The function should achieve a time complexity of O(n√m), where n is the length of the list and m is the largest number in the list, and should not use any external libraries or functions to check for prime numbers.
"""

def largest_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_prime_number = -1
    for num in numbers:
        if is_prime(num) and num > largest_prime_number:
            largest_prime_number = num
    return largest_prime_number