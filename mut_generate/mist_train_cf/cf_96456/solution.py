"""
QUESTION:
Write a function `maximum_product(arr)` that finds the maximum product of any three distinct numbers in the given array `arr`. The array has at least 6 numbers. The solution must have a time complexity less than O(n^2).
"""

def maximum_product(arr):
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    for num in arr:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2 and num < max1:
            max3 = max2
            max2 = num
        elif num > max3 and num < max2:
            max3 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2 and num > min1:
            min2 = num

    return max(max1 * max2 * max3, min1 * min2 * max1)