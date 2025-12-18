"""
QUESTION:
Write a function `find_second_smallest(nums)` that takes a list of integers `nums` as input and returns the second smallest element in the list. The function should not use any built-in sorting functions or data structures and should have a time complexity of O(n), where n is the length of the list. The function should iterate through the list only once.
"""

def find_second_smallest(nums):
    smallest = float('inf')
    second_smallest = float('inf')
    
    for num in nums:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    
    return second_smallest