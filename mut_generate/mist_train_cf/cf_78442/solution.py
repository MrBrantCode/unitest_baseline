"""
QUESTION:
Write a function `getMaximumGenerated(n)` that generates an array `nums` of length `n + 1` based on the following rules:
- `nums[0] = 0`
- `nums[1] = 1`
- `nums[2 * i] = nums[i]`
- `nums[2 * i + 1] = nums[i] + nums[i + 1]`
The function should return a tuple containing the maximum integer in the array `nums` and its index. The input `n` is an integer such that `0 <= n <= 100`.
"""

def getMaximumGenerated(n):
    if n == 0:
        return (0, 0)
    nums = [0]*(n+1)
    nums[1] = 1
    for i in range(2, n+1):
        if i % 2 == 0:
            nums[i] = nums[i//2]
        else:
            nums[i] = nums[i//2] + nums[i//2+1]
    max_value, max_index = max((v, i) for i, v in enumerate(nums))
    return (max_value, max_index)