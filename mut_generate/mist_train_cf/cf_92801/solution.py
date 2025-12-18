"""
QUESTION:
Write a function called `max_product(arr)` that finds the maximum product of any three distinct numbers in the given array. The array will have at least 6 numbers. The function should not use sorting or nested loops.
"""

def max_product(arr):
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = min3 = float('inf')

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

        if num < min1:
            min3 = min2
            min2 = min1
            min1 = num
        elif num < min2:
            min3 = min2
            min2 = num
        elif num < min3:
            min3 = num

    return max(max1 * max2 * max3, max1 * min1 * min2)