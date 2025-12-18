"""
QUESTION:
Write a function `find_second_smallest` that takes an array of integers as input. The function should return the second smallest element in the array. If the array has less than two elements, the function should return None. The function should assume that the input array may contain duplicate elements.
"""

def entance(nums):
    if len(nums) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in nums:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None