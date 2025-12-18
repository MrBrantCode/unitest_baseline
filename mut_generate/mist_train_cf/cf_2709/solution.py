"""
QUESTION:
Write a function that takes an array of positive integers as input and returns the maximum and second maximum prime numbers in the array. The array will have at least 5 elements and at most 1000 elements, and the maximum value of any element will not exceed 10^6. If there is no prime number or only one prime number in the array, output the maximum prime number found and 0.
"""

import math

def entrance(nums):
    """
    This function takes an array of positive integers as input and returns 
    the maximum and second maximum prime numbers in the array.

    Args:
    nums (list): A list of positive integers.

    Returns:
    tuple: A tuple containing the maximum and second maximum prime numbers.
    """

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    maxPrime = 0
    secondMaxPrime = 0

    for num in nums:
        if is_prime(num):
            if num > maxPrime:
                secondMaxPrime = maxPrime
                maxPrime = num
            elif num > secondMaxPrime and num != maxPrime:
                secondMaxPrime = num

    return maxPrime, secondMaxPrime