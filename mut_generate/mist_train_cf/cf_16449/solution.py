"""
QUESTION:
Create a function `find_sum_of_squares_pairs(arr)` that takes an array of integers `arr` as input and returns a list of pairs of numbers that can be expressed as the sum of two squares, such that the sum is also a prime number. The function should consider all possible pairs of numbers in the array, without regard to order, and include all pairs with the same sum in the output.
"""

import math

def find_sum_of_squares_pairs(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_sum_of_squares(n):
        for i in range(int(math.sqrt(n)) + 1):
            if math.isqrt(n - i*i)**2 == (n - i*i):
                return True
        return False

    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            num1 = arr[i]
            num2 = arr[j]
            if is_prime(num1 + num2) and is_sum_of_squares(num1 + num2):
                result.append((num1, num2))
    return result