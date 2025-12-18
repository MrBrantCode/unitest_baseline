"""
QUESTION:
Implement the `maxRotateFunction` function to calculate the maximum value of the rotation function `F(k)` for the array `nums` after performing all operations in `ops`. The function `F(k)` is defined as the sum of the products of the indices and values of the array obtained by rotating `nums` by `k` positions clockwise. The function should return a tuple containing the maximum value of `F(k)` and the corresponding `k` value.

Restrictions:
- `n == nums.length`
- `1 <= n <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `m == ops.length`
- `0 <= m <= 10^5`
- `0 <= ops[i][0] < n`
- `-2^31 <= ops[i][1] <= 2^31 - 1`
"""

def maxRotateFunction(nums):
    n = len(nums)
    total_sum = sum(nums)
    f = sum(i * num for i, num in enumerate(nums))
    max_f = f
    
    for k in range(1, n):
        f = f + total_sum - n * nums[n-k]
        max_f = max(max_f, f)
    
    return max_f