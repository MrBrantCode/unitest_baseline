"""
QUESTION:
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:


int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""

import random

def pick_random_index(nums, target):
    first_idx = None
    idx_count = 0
    
    for i in range(len(nums)):
        if nums[i] == target:
            if first_idx is None:
                first_idx = i
            idx_count += 1
    
    if idx_count > 0:
        return int(idx_count * random.random() // 1) + first_idx