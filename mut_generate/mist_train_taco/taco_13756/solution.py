"""
QUESTION:
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:


Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8


Note:


       The array is only modifiable by the update function.
       You may assume the number of calls to update and sumRange function is distributed evenly.
"""

import math

def init_num_array(nums):
    step = 20
    cache = [0] * math.ceil(len(nums) / step)
    for i in range(len(nums)):
        cache[i // step] += nums[i]
    return {
        'nums': nums,
        'step': step,
        'cache': cache
    }

def update_num_array(num_array, i, val):
    old = num_array['nums'][i]
    num_array['nums'][i] = val
    num_array['cache'][i // num_array['step']] += val - old
    return num_array

def sum_range_num_array(num_array, i, j):
    step = num_array['step']
    nums = num_array['nums']
    cache = num_array['cache']
    
    if j // step - i // step > 1:
        spliti = (i // step + 1) * step - 1
        splitj = j // step * step
        sumi = sum(nums[i:spliti + 1])
        sumj = sum(nums[splitj:j + 1])
        sumbetween = sum(cache[i // step + 1:j // step])
        return sumi + sumj + sumbetween
    else:
        return sum(nums[i:j + 1])