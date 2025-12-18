"""
QUESTION:
Implement a function `find_duplicate(nums)` that takes a list of integers as input where each integer is in the range [1, n] and n is the length of the list. The list contains a single duplicate number. The function should return the duplicate number with a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list.
"""

def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    ptr1 = nums[0]
    ptr2 = slow

    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1