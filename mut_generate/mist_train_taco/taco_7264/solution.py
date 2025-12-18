"""
QUESTION:
Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.


 
Example 1:
Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:
Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.

Example 3:
Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).

 
Constraints:

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4
"""

from collections import defaultdict
from typing import List

def helper(l1: List[int], l2: List[int]) -> int:
    if len(l1) < 1 and len(l2) < 2:
        sum_remove = 0
    elif len(l1) < 1:
        sum_remove = min(l2)
        l2.remove(sum_remove)
        sum_remove += min(l2)
    elif len(l2) < 2:
        sum_remove = min(l1)
    else:
        sum_remove1 = min(l1)
        sum_remove2 = min(l2)
        l2.remove(sum_remove2)
        sum_remove2 += min(l2)
        sum_remove = min(sum_remove1, sum_remove2)
    return sum_remove

def max_sum_divisible_by_three(nums: List[int]) -> int:
    sum_nums = sum(nums)
    mod3_sum_nums = sum_nums % 3
    if mod3_sum_nums == 0:
        return sum_nums
    mod3_dict = defaultdict(list)
    for num in nums:
        mod3_dict[num % 3].append(num)
    if mod3_sum_nums == 1:
        sum_remove = helper(mod3_dict[1], mod3_dict[2])
    else:
        sum_remove = helper(mod3_dict[2], mod3_dict[1])
    if sum_remove > 0:
        return sum_nums - sum_remove
    else:
        return 0