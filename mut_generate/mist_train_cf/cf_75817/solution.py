"""
QUESTION:
Write a function named `increasingQuadruplet` that takes an integer array `nums` as input and returns `true` if there exists a quadruplet of indices `(i, j, k, l)` that adhere to the conditions `i < j < k < l` and `nums[i] < nums[j] < nums[k] < nums[l]`, and `false` otherwise. The function must operate within `O(n)` time complexity and `O(1)` space complexity. The input array `nums` has a length of at least 1 and at most 10^5, and each element `nums[i]` is an integer in the range `-2^31 <= nums[i] <= 2^31 - 1`.
"""

def increasingQuadruplet(nums):
    c1 = c2 = c3 = float('inf')
    for num in nums:
        if num <= c1:
            c1 = num
        elif num <= c2:
            c2 = num
        elif num <= c3:
            c3 = num
        else:
            return True
    return False