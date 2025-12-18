"""
QUESTION:
Write a function named `find_second_highest_prime` that takes an array of positive integers as input and returns the second highest prime number in the array. The function should not use the built-in `max()` or `sort()` functions, and its time complexity should be O(n), where n is the length of the array.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_second_highest_prime(arr):
    highest_prime = float('-inf')
    second_highest_prime = float('-inf')

    for num in arr:
        if is_prime(num):
            if num > highest_prime:
                second_highest_prime = highest_prime
                highest_prime = num
            elif num > second_highest_prime and num != highest_prime:
                second_highest_prime = num

    return second_highest_prime