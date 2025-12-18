"""
QUESTION:
Write a function `find_smallest_and_largest(nums)` that takes an unsorted list of numbers `nums` as input. The function should return a tuple containing the smallest number, the largest number, the count of the smallest number, and the count of the largest number. The function should have a time complexity of O(n) and should not use any built-in sorting functions.
"""

def find_smallest_and_largest(nums):
    smallest = float('inf')
    largest = float('-inf')
    smallest_count = 0
    largest_count = 0

    for num in nums:
        if num < smallest:
            smallest = num
            smallest_count = 1
        elif num == smallest:
            smallest_count += 1

        if num > largest:
            largest = num
            largest_count = 1
        elif num == largest:
            largest_count += 1

    return smallest, largest, smallest_count, largest_count