"""
QUESTION:
Write a function `majorityElement(nums)` that finds the majority element in an array using the Boyer-Moore Voting Algorithm. The majority element is defined as the element that appears more than ⌊ n/2 ⌋ times in the array of size n, where it is guaranteed to exist. The function should return the majority element and have a time complexity of O(n) and space complexity of O(1).
"""

def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate