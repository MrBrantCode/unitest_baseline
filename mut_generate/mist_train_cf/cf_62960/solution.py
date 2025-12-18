"""
QUESTION:
Write a function `threeSumSmaller(nums, target)` that takes a list of integers `nums` and an integer `target` as input and returns the number of index triplets `i`, `j`, `k` with `0 <= i < j < k < n` that satisfy the condition `nums[i] + nums[j] + nums[k] < target`, where `n` is the length of `nums`. The triplets must also satisfy two constraints: the sum of the indices `(i + j + k)` must be an even number, and the triplet `(nums[i], nums[j], nums[k])` must be in ascending order. The function should run in `O(n^2)` time complexity.
"""

def threeSumSmaller(nums, target):
    nums.sort()
    n = len(nums)
    cnt = 0
    for i in range(n-2):        
        if (i%2 == 0):  # Only consider even indices for i
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < target and (i + j + k)%2 == 0:  # Ensure the sum of indices is even
                    cnt += k - j  # The number of triplets from j to k indices
                    j += 1  # Move the j pointer forward
                else:
                    k -= 1  # Move the k pointer backward if sum >= target
    return cnt