"""
QUESTION:
Given a non-negative integer array `nums` and an integer `m`, write a function `splitArray(nums, m)` to split `nums` into `m` non-empty continuous subarrays such that no two subarrays have the same sum and the largest sum among these `m` subarrays is minimized. 

`nums` and `m` are subject to the following constraints: `1 <= len(nums) <= 1000`, `0 <= nums[i] <= 10^6`, and `1 <= m <= min(50, len(nums))`.
"""

def splitArray(nums, m):
    prefix = [0]*(len(nums)+1)
    for i in range(len(nums)):
        prefix[i+1] = prefix[i] + nums[i]

    def check(mid):
        cnt = 1
        total = 0
        vis = set()
        for i in range(1, len(nums)+1):
            if total + nums[i-1] > mid:
                total = nums[i-1]
                cnt += 1
                if total in vis:
                    return False
                vis.add(total)
            else:
                total += nums[i-1]
                if total in vis:
                    return False
            if total == mid:
                total = 0
        return cnt <= m and not total

    l, r = max(nums), prefix[-1]
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid + 1
    return l