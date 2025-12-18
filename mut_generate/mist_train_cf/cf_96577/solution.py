"""
QUESTION:
Write a function `find_highest_prime` that takes an array of integers as input and returns the highest prime number in the array. If no prime numbers are found, return -1. The function should use a recursive approach and helper function to check if a number is prime. The function should not take any other arguments besides the array, so any recursive calls should utilize default parameters.
"""

def is_prime(num, div=2):
    # Base cases
    if num <= 1:
        return False
    if div * div > num:
        return True
    if num % div == 0:
        return False
    
    # Recursive case
    return is_prime(num, div + 1)

def find_highest_prime(arr, index=0, highest=-1):
    # Base case
    if index == len(arr):
        return highest
    
    # Recursive case
    num = arr[index]
    if is_prime(num) and num > highest:
        highest = num
    
    return find_highest_prime(arr, index + 1, highest)