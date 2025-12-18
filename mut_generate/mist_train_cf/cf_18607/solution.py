"""
QUESTION:
Write a function called `sort_prime_numbers` that takes three arrays of integers as input, classifies each element as either prime or not prime, calculates the sum of divisors for each prime number, and returns the prime numbers sorted in descending order based on the sum of their divisors. The function should not use any built-in functions or libraries to check for prime numbers and should have a time complexity of O(n^2) or better.
"""

import math

def sort_prime_numbers(arr1, arr2, arr3):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_divisors(n):
        div_sum = 0
        for i in range(1, n + 1):
            if n % i == 0:
                div_sum += i
        return div_sum

    prime_numbers = []
    for arr in [arr1, arr2, arr3]:
        for num in arr:
            if is_prime(num):
                prime_numbers.append(num)

    n = len(prime_numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sum_of_divisors(prime_numbers[j]) < sum_of_divisors(prime_numbers[j + 1]):
                prime_numbers[j], prime_numbers[j + 1] = prime_numbers[j + 1], prime_numbers[j]
    return prime_numbers