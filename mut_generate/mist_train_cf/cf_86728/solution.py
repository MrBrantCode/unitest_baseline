"""
QUESTION:
Create a function called `find_minimum_positive_odd` that takes an array of integers as input and returns the minimum positive odd number in the array. The array will always contain at least one positive odd number. If there are multiple minimum positive odd numbers, return the one with the lowest index. Assume the array only contains integers between -100 and 100, inclusive.
"""

def find_minimum_positive_odd(arr):
    min_odd = float('inf')

    for num in arr:
        if num > 0 and num % 2 != 0 and num < min_odd:
            min_odd = num

    return min_odd