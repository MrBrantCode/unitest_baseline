"""
QUESTION:
Create a function `filter_prime_numbers` that takes an array of numbers as input and returns a new array containing only the prime numbers from the input array. The input array can contain positive, negative, floating-point, and complex numbers. The function should not modify the original array and should have a time complexity of O(n*sqrt(k)), where n is the length of the input array and k is the maximum absolute value of the numbers in the array.
"""

import math

def filter_prime_numbers(numbers):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    prime_numbers = []
    for num in numbers:
        if isinstance(num, (int, float, complex)) and is_prime(abs(num)):
            prime_numbers.append(num)
    return prime_numbers