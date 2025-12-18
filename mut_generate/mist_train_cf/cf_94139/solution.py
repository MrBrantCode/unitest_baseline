"""
QUESTION:
Write a function called `find_smallest_prime` that takes a list of positive integers as input and returns the smallest prime number in the list. If no prime number is found, return -1. The function should have a time complexity of O(n√m), where n is the length of the list and m is the largest number in the list, without using any external libraries or additional memory space apart from the input list and a few variables for iteration.
"""

def find_smallest_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    smallest_prime = -1
    for num in numbers:
        if is_prime(num):
            if smallest_prime == -1 or num < smallest_prime:
                smallest_prime = num
    return smallest_prime