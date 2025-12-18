"""
QUESTION:
Write a function `contains_duplicate` that checks if a list of integers contains duplicate values or not. The function should handle both positive and negative integers, have a time complexity of O(n), and a space complexity of O(n) due to the set used in the solution. The function should return True if the list contains any duplicate values and False otherwise.
"""

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False