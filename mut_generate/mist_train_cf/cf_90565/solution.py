"""
QUESTION:
Write a function `find_second_smallest_prime(arr)` that takes an array of integers as input and prints the second smallest prime number greater than 100. The function should have a time complexity of O(n), where n is the size of the array, and should not use any extra space other than the variables required for the algorithm. If no second smallest prime number greater than 100 exists, print a corresponding message.
"""

import sys

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_second_smallest_prime(arr):
    smallest_prime = sys.maxsize
    second_smallest_prime = sys.maxsize

    for num in arr:
        if num > 100 and is_prime(num):
            if num < smallest_prime:
                second_smallest_prime = smallest_prime
                smallest_prime = num
            elif num < second_smallest_prime and num != smallest_prime:
                second_smallest_prime = num

    if second_smallest_prime == sys.maxsize:
        print("No second smallest prime greater than 100 found")
    else:
        print("Second smallest prime greater than 100 is:", second_smallest_prime)