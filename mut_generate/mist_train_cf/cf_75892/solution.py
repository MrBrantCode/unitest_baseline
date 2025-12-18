"""
QUESTION:
Write a function `containsNearbyAlmostDuplicate` that takes in a list of strings where each string contains comma-separated integers, an integer k, and a target integer t. The function should return True if there exist two indices i and j in any of the sub-lists of integers, such that the absolute difference between i and j is less than or equal to k, and the absolute difference between the values at indices i and j is less than or equal to t. Otherwise, it should return False.
"""

def containsNearbyAlmostDuplicate(nums, k, t):
    for ix, sublist in enumerate(nums):
        nums[ix] = [int(num) for num in sublist.split(',')]
    for ix, sublist in enumerate(nums):
        for i in range(len(sublist)):
            for j in range(i+1, min(i+k+1, len(sublist))):
                if abs(sublist[i]-sublist[j]) <= t:
                    return True
    return False