"""
QUESTION:
Write a function named `maximum_product` that finds the maximum product of three numbers in an array, where at least one of the numbers must be negative. Return 0 if no such triplet exists. The function should have a time complexity of O(n) or better and a space complexity of O(1) or better, without modifying the original array. The function should handle edge cases such as an array with less than three elements or an array with all positive numbers.
"""

def maximum_product(nums):
    max1 = float('-inf')
    max2 = float('-inf')
    max3 = float('-inf')
    min1 = float('inf')
    min2 = float('inf')

    for num in nums:
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

    if min1 >= 0:
        return 0

    return max(max1 * max2 * max3, max1 * min1 * min2)