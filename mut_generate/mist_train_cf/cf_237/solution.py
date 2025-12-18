"""
QUESTION:
Create a function named `remove_duplicates` that takes a list of integers as input and returns the list with duplicates removed. The function should have a time complexity of O(n log n) or better and a space complexity of O(n) or better. It cannot use any built-in Python functions or libraries, and it must preserve the original order of the elements. The input list can contain up to 10^6 integers, and each integer can range from -10^9 to 10^9.
"""

def remove_duplicates(nums):
    unique_nums = set()
    result = []

    for num in nums:
        if num not in unique_nums:
            unique_nums.add(num)
            result.append(num)

    return result