"""
QUESTION:
Write a function named `find_second_smallest_odd_prime` that takes an array of positive integers as input and returns the second smallest odd prime number in the array. If no such number exists, the output should be the actual value returned by the function.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_second_smallest_odd_prime(arr):
    smallest = float('inf')
    second_smallest = float('inf')

    for num in arr:
        if is_prime(num) and num % 2 != 0:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest:
                second_smallest = num

    return second_smallest