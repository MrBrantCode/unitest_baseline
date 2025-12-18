"""
QUESTION:
Write a function `countTriplets(nums, low, high)` that takes a list of integers `nums` and two integers `low` and `high` as input. The function should return the number of nice triplets in the list, where a nice triplet is a triplet `(i, j, k)` such that `0 <= i < j < k < nums.length` and `low <= (nums[i] AND nums[j] AND nums[k]) <= high`. The function should have a time complexity of O(n + MAX), where n is the number of elements in `nums` and MAX is the maximum possible value of the bitwise AND operation. The constraints are `1 <= nums.length <= 2 * 10^4`, `1 <= nums[i] <= 2 * 10^4`, and `1 <= low <= high <= 2 * 10^4`.
"""

def countTriplets(nums, low: int, high: int) -> int:
    n = len(nums)
    bit = 14
    MAX = 1<<bit
    dp = [0]*MAX
    pre = [0] * (MAX + 1)
    
    for num in nums: dp[num] += 1
        
    for i in range(MAX): pre[i+1] = pre[i] + dp[i]
    
    def count(x):
        res = 0
        for num in nums:
            res += pre[x^num+1] if x^num < MAX else n
            res -= pre[num]
        return res//3
    
    return count(high+1) - count(low)