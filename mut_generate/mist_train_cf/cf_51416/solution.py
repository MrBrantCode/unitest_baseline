"""
QUESTION:
Write a function `first_unique_prime` that finds and returns the first unique prime number in a given list of integers. A unique number is a number that appears only once in the list, and a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. If no such number exists, return None.
"""

def first_unique_prime(numbers):
    def is_prime(num):
        if num == 1:
            return False
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True

    for num in numbers:
        if numbers.count(num) == 1 and is_prime(num):
            return num
    return None