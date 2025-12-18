"""
QUESTION:
Write a function `find_duplicates` that takes a list of integers `nums` and returns a list of all duplicate numbers in `nums`. The function should maintain the original order of numbers and have a time complexity of O(n) and space complexity of O(n), without using built-in functions, libraries, or extra space except for the output list.
"""

def find_duplicates(nums):
    num_set = set()
    duplicate_nums = []
    duplicate_set = set()

    for num in nums:
        if num in num_set and num not in duplicate_set:
            duplicate_nums.append(num)
            duplicate_set.add(num)
        num_set.add(num)

    return duplicate_nums