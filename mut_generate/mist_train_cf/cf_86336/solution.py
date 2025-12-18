"""
QUESTION:
Create a function named `remove_duplicates` that takes a list of integers as input and returns a list of unique integers from the input list. The function should have a time complexity of O(n log n) or better and a space complexity of O(n) or better. The input list can contain up to 10^6 integers, and each integer can range from -10^9 to 10^9. Do not use any built-in Python functions or libraries, except for basic data types like lists and sets.
"""

def remove_duplicates(nums):
    unique_nums = set()
    result = []

    for num in nums:
        if num not in unique_nums:
            unique_nums.add(num)
            result.append(num)

    return result