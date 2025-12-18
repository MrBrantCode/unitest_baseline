"""
QUESTION:
Write a function named `find_max_num` that finds the maximum number in a given list while ignoring negative numbers and numbers that are divisible by 3. The function should handle lists of any length and cases where the list may contain duplicates.
"""

def find_max_num(nums):
    max_num = float('-inf')  # Initialize max_num with a very small value

    for num in nums:
        if num > 0 and num % 3 != 0:  # Ignore negative numbers and numbers divisible by 3
            max_num = max(max_num, num)

    return max_num