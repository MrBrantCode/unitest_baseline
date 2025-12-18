"""
QUESTION:
Write a program that contains two functions: `check_prime(num)` and `calculate_median(arr)`. The `calculate_median(arr)` function should take an array of numbers as input and return its median. The `check_prime(num)` function should take a number as input and return True if it is a prime number and False otherwise. The `calculate_median(arr)` function should sort the array and calculate the median depending on whether the number of elements in the array is odd or even. The `check_prime(num)` function should check for divisibility starting from 2 to the square root of the number.
"""

def check_prime(num):
    if num < 2: 
        return False
    if num == 2: 
        return True
    if num % 2 == 0:
        return False
    for current in range(3, int(num ** 0.5) + 1, 2):
        if num % current == 0:
            return False
    return True

def calculate_median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        median1 = arr[n//2]
        median2 = arr[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = arr[n//2]
    return median