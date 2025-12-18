"""
QUESTION:
Implement a function `max_product(nums)` that takes a list of positive integers `nums` and returns the maximum product of any four distinct integers in the list. The function should have a time complexity of O(n), where n is the length of the input list, and a space complexity of O(1).
"""

def max_product(nums):
    max1 = max2 = max3 = max4 = float('-inf')
    min1 = min2 = float('inf')

    for num in nums:
        if num > max1:
            max4 = max3
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max4 = max3
            max3 = max2
            max2 = num
        elif num > max3:
            max4 = max3
            max3 = num
        elif num > max4:
            max4 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    return max(max1 * max2 * max3 * max4, max1 * min1 * min2 * max2)