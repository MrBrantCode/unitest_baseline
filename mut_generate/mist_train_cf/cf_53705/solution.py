"""
QUESTION:
Find the K-th smallest distance and the number of pairs with that distance in a given integer array. The distance of a pair (A, B) is defined as the absolute difference between A and B. The function should return a tuple containing the K-th smallest distance and the number of pairs with that distance.

Given an integer array nums and an integer k, where 2 <= len(nums) <= 10000, 0 <= nums[i] < 1000000, and 1 <= k <= len(nums) * (len(nums) - 1) / 2.
"""

def smallestDistancePair(nums, k):
    def pair_count(mid):
        count, pairs = 0, 0
        for i in range(len(nums)):
            j = i + 1
            while (j < len(nums) and nums[j] - nums[i] <= mid):
                if nums[j] - nums[i] == mid:
                    pairs += 1
                j += 1
                count += j - i - 1
        return count, pairs

    nums.sort()
    left, right = 0, nums[-1] - nums[0]
    
    while left < right:
        mid = (left + right) // 2
        count, _ = pair_count(mid)
        if count >= k:
            right = mid
        else:
            left = mid + 1

    _, pairs_mid = pair_count(left)
    return (left, pairs_mid)