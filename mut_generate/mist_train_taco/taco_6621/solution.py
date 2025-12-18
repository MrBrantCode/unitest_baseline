"""
QUESTION:
Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B. 

Example 1:

Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.



Note:

2 .
0 .
1 .
"""

def find_kth_smallest_distance(nums: list[int], k: int) -> int:
    nums.sort()
    (l, r) = (0, nums[-1] - nums[0])
    while l < r:
        m = l + (r - l) // 2
        count = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > m:
                left += 1
            count += right - left
        if count < k:
            l = m + 1
        else:
            r = m
    return l