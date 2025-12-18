"""
QUESTION:
Write a function `find_top_3_highest_numbers` that takes an array of integers as input and returns the top 3 highest numbers without using any sorting algorithm or built-in functions that directly solve the problem. The input array can have a maximum of 1000 elements.
"""

def find_top_3_highest_numbers(arr):
    max1 = float('-inf')
    max2 = float('-inf')
    max3 = float('-inf')

    for num in arr:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num

    return [max1, max2, max3]