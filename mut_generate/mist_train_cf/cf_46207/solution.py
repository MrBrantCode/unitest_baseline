"""
QUESTION:
Write a function `majorityElement(nums)` that takes a list of integers `nums` and returns all the majority elements that appear more than `⌊n / 3⌋` times, where `n` is the length of `nums`. Assume that `nums` always has a majority element and there can be at most two majority elements that appear more than `n/3` times. The function should run in linear time and use `O(1)` space.
"""

def majorityElement(nums):
    if not nums:
        return []
    count1, count2, candidate1, candidate2 = 0, 0, 0, 1
    for n in nums:
        if n == candidate1:
            count1 += 1
        elif n == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = n, 1
        elif count2 == 0:
            candidate2, count2 = n, 1
        else:
            count1, count2 = count1 - 1, count2 - 1
    return [n for n in (candidate1, candidate2)
            if nums.count(n) > len(nums) // 3]