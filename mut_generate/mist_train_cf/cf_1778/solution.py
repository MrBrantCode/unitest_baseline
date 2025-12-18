"""
QUESTION:
Write a function named `sum_of_elements` that takes an array of integers as input and returns the sum of elements that are divisible by both 2 and 3, are prime numbers, and have a sum of digits that is also a prime number.
"""

def sum_of_elements(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = 0
    for num in arr:
        if num % 2 == 0 and num % 3 == 0 and is_prime(num) and is_prime(sum(int(digit) for digit in str(num))):
            result += num
    return result