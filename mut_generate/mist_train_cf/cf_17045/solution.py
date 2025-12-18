"""
QUESTION:
Write a function `find_max_and_second_max` that takes a list of integers as input, and returns a tuple containing the maximum and second maximum elements in the list. The function should not use any built-in functions or libraries to find the maximum or second maximum elements. The list may contain both positive and negative integers, and may have duplicate values. The function should have a time complexity of O(n), where n is the length of the list.
"""

def find_max_and_second_max(nums):
    # Initialize max1 and max2 with the smallest possible values
    max1 = float('-inf')
    max2 = float('-inf')

    # Iterate through each number in the list
    for num in nums:
        # If current number is greater than max1, update max1 and max2
        if num > max1:
            max2 = max1
            max1 = num
        # If current number is between max2 and max1, update max2
        elif num > max2 and num != max1:
            max2 = num

    # Return both the maximum and second maximum elements
    return max1, max2