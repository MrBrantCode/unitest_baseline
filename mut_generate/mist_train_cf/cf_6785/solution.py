"""
QUESTION:
Write a function named PrimeNumbers that takes a list of integers as input and returns a list of prime numbers from the input list. The function should have a runtime complexity of O(n^2), where n is the length of the input list. The function should return an empty list if the input list is empty.
"""

def PrimeNumbers(items):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    prime_nums = [num for num in items if is_prime(num)]
    return prime_nums