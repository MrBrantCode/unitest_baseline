"""
QUESTION:
Design a function named `find_second_smallest_largest` that accepts an array of integers. The function should sort the array and return the second smallest and the second largest numbers. If the array has less than 4 unique elements, return 'None' for the second smallest/largest number. The function should handle exceptions for cases where the input is not a list, the list is empty, or the list contains non-integer elements. Implement the function without using built-in sorting functions, instead using if-else statements or loops.
"""

def find_second_smallest_largest(nums):
    if not isinstance(nums, list):
        return 'Input should be a list'
    if not nums:
        return 'List should not be empty'
    if not all(isinstance(num, int) for num in nums):
        return 'All elements in list should be integers'

    # Bubble sort
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    distinct_nums = list(set(nums))  # Remove duplicates

    if len(distinct_nums) < 2:
        return 'List should contain at least two distinct numbers'
    if len(distinct_nums) < 4:
        second_smallest = second_largest = None
    else:
        second_smallest = distinct_nums[1]
        second_largest = distinct_nums[-2]

    return second_smallest, second_largest