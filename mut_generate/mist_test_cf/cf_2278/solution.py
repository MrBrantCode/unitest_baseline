"""
QUESTION:
Create a function `replace_second_smallest_prime` that takes an array of positive integers as input and returns the modified array where the second smallest prime number is replaced with the sum of all prime numbers in the array. The function should have a time complexity of O(nlogn). If there is no second smallest prime number in the array, the original array should be returned unchanged.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def replace_second_smallest_prime(arr):
    smallest_prime = float('inf')
    second_smallest_prime = float('inf')
    prime_sum = 0

    for num in arr:
        if is_prime(num):
            prime_sum += num
            if num < smallest_prime:
                second_smallest_prime = smallest_prime
                smallest_prime = num
            elif num < second_smallest_prime and num != smallest_prime:
                second_smallest_prime = num
    
    if second_smallest_prime != float('inf'):
        for i in range(len(arr)):
            if arr[i] == second_smallest_prime:
                arr[i] = prime_sum
    
    return arr