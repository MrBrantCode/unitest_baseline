"""
QUESTION:
Write a function `max_product_of_three` that takes an array of integers as input and returns the maximum product of three numbers in the array. The input array is guaranteed to have at least three integers. The function should be optimized for performance, with a time complexity of O(n), where n is the number of elements in the array.
"""

def max_product_of_three(nums):
    if len(nums) < 3:
        raise Exception('Less than 3 items')
    
    # Initialize maximum and minimum trackers
    max_1, max_2, max_3 = float('-inf'), float('-inf'), float('-inf')
    min_1, min_2 = float('inf'), float('inf')
    
    # Scan the numbers in the list
    for num in nums:
        # If the current number is larger than the largest number
        if num > max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = num
        # If the current number is the second largest
        elif num > max_2:
            max_3 = max_2
            max_2 = num
        # If the current number is the third largest
        elif num > max_3:
            max_3 = num
            
        # If the current number is smaller than the smallest number
        if num < min_1:
            min_2 = min_1
            min_1 = num
        # If the current number is the second smallest
        elif num < min_2:
            min_2 = num
            
    # Return the maximum product
    return max(max_1 * max_2 * max_3, max_1 * min_1 * min_2)