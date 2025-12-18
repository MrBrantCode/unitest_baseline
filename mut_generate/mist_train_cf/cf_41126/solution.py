"""
QUESTION:
Implement a function `count_pairs(nums)` that takes a list of integers `nums` as input and returns the number of pairs of indices `(i, j)` such that `i < j` and `nums[i] + nums[j]` is a power of 2. The function should run efficiently for large inputs. The input list `nums` will contain integers up to 2^21.
"""

from collections import defaultdict
from typing import List

def count_pairs(nums: List[int]) -> int:
    power_of_two = set(2 ** i for i in range(22))  

    count_map = defaultdict(int)
    pairs_count = 0

    for num in nums:
        for power in power_of_two:
            complement = power - num
            pairs_count += count_map[complement]
        count_map[num] += 1

    return pairs_count