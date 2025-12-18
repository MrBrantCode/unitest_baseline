"""
QUESTION:
Write a function `group_by_distance(nums, distance)` where `nums` is a sorted list of integers and `distance` is the maximum allowed distance between integers in a set. The function should return a list of sets, where each set contains integers that are within the specified distance of each other. The input list `nums` has a length between 1 and 10^5 and the distance is between 1 and 10^9.
"""

from typing import List

def group_by_distance(nums: List[int], distance: int) -> List[List[int]]:
    sets = []
    current_set = []

    for num in nums:
        if not current_set:
            current_set.append(num)
        else:
            if num - current_set[-1] <= distance:
                current_set.append(num)
            else:
                sets.append(current_set)
                current_set = [num]

    if current_set:
        sets.append(current_set)

    return sets