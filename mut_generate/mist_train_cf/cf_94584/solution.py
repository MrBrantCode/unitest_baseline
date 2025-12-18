"""
QUESTION:
Write a function `replace_second_smallest_prime` that takes an array of positive integers as input. The function should find the second smallest prime number in the array and replace it with the sum of all the prime numbers in the array. If no prime numbers or only one prime number exists in the array, return -1.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def replace_second_smallest_prime(arr):
    prime_sum = 0

    for num in arr:
        if is_prime(num):
            prime_sum += num

    if prime_sum == 0:
        return -1

    smallest = float('inf')
    second_smallest = float('inf')

    for num in arr:
        if is_prime(num):
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest:
                second_smallest = num

    if second_smallest == float('inf'):
        return -1

    arr[arr.index(second_smallest)] = prime_sum

    return arr