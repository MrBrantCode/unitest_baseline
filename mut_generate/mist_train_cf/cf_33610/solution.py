"""
QUESTION:
Write a function `highest_product_of_three(nums)` that takes a list of integers `nums` as input and returns the highest product of three distinct numbers from the list. The input list `nums` will contain at least three integers and may contain both positive and negative integers.
"""

def highest_product_of_three(nums):
    max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
    min1, min2 = float('inf'), float('inf')

    for num in nums:
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

    return max(max1 * max2 * max3, min1 * min2 * max1)