"""
QUESTION:
Write a function named `find_max_prime` that reads a list of positive integers from standard input and returns the maximum prime number in the list. The input list size is provided as the first input value, followed by the actual list elements. Assume that the input values are positive integers.
"""

import math

def find_max_prime(arr):
    # Initialize the maximum prime number to 0
    maxPrime = 0

    # Iterate through each element of the array
    for num in arr:
        # Check if the number is prime
        isPrime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                isPrime = False
                break

        # If the number is prime and greater than maxPrime, update maxPrime
        if isPrime and num > maxPrime and num > 1:
            maxPrime = num

    return maxPrime