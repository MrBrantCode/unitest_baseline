"""
QUESTION:
Write a function named `max_product_of_three` that takes an array of numbers as input and returns the maximum product of any three distinct numbers in the array. The function should not use sorting or nested loops and should have a time complexity less than O(n^2). The function should handle negative numbers and zeros in the array.
"""

def max_product_of_three(arr):
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

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
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    max_product_1 = max1 * max2 * max3
    max_product_2 = max1 * min1 * min2

    return max(max_product_1, max_product_2)