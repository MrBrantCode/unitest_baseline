"""
QUESTION:
Write a function named `find_second_smallest_odd_prime` that takes an integer array as input and returns the second smallest odd prime number in the array. The array will only contain positive numbers. The function should return the second smallest odd prime number if it exists, otherwise return infinity.
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
            elif num < second_smallest and num > smallest:
                second_smallest = num

    return second_smallest