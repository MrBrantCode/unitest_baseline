"""
QUESTION:
Create a function `filter_and_transform` that takes an array of integers as input. The function should return an array containing only the numbers from the input array that are divisible by 3. However, if the input array does not contain any numbers divisible by 3, the function should return an array containing the square roots of the original numbers. The function should also handle the case where the input array is empty.
"""

import math

def filter_and_transform(arr):
    # Filter numbers that are divisible by 3
    divisible_by_three = list(filter(lambda x: x % 3 == 0, arr))
    
    # If the filtered list is not empty, return it
    if len(divisible_by_three) > 0:
        return divisible_by_three
    # If the filtered list is empty, return the square roots of the original numbers
    else:
        return [math.sqrt(x) for x in arr]