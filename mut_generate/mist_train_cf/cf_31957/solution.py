"""
QUESTION:
Write a function `containsDuplicate(nums)` that determines if a list of integers contains any duplicates. The function should return True if duplicates exist and False otherwise.

The function must meet the following conditions:
- The input list `nums` will contain between 1 and 10^5 integers.
- Each integer in the list will be between -10^9 and 10^9 (inclusive).
- The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False