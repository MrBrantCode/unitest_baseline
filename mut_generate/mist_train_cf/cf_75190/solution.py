"""
QUESTION:
Given a non-empty array of non-negative integers `nums` and an integer `m`, write a function `splitArray` that splits the array into `m` non-empty continuous subarrays such that the sum of the elements in each subarray is a prime number. The function should return the minimum largest sum among these `m` subarrays.

The function `splitArray` should take two parameters: `nums` (a list of integers) and `m` (an integer). The constraints are: `1 <= len(nums) <= 1000`, `0 <= nums[i] <= 10^6`, and `1 <= m <= min(50, len(nums))`.
"""

def splitArray(nums, m):
    import math
    def prime(n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def check(mid):
        cnt = 0
        s = 0
        for num in nums:
            if s + num <= mid and prime(s + num):
                s += num
            else:
                s = num
                cnt += 1
        return cnt

    l, r = max(nums), sum(nums)
    while l < r:
        mid = (l + r) // 2
        if prime(mid) and check(mid) <= m - 1:
            r = mid
        else:
            l = mid + 1
    return l