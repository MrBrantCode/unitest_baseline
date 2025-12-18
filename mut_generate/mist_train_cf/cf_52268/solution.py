"""
QUESTION:
Write a function `minSubarray(nums, p)` that takes an array of positive integers `nums` and an integer `p` as input, and returns the length of the smallest subarray that needs to be removed so that the product of the remaining elements is divisible by `p`, or `-1` if it is impossible. The length of `nums` is between 1 and 10^5, and each element in `nums` and `p` is between 1 and 10^9. It is not allowed to remove the whole array.
"""

def minSubarray(nums, p):
    n, r = len(nums), sum(nums) % p
    if r == 0: return 0
    prefix, postfix, min_len = {0: -1}, {0: n}, n+1
    cur = 0
    for i in range(n):
        cur = (cur + nums[i]) % p
        min_len = min(min_len, i - prefix.get((cur-r) % p, -n))
        prefix[cur] = i
    cur = 0
    for i in range(n-1, -1, -1):
        cur = (cur + nums[i]) % p
        min_len = min(min_len, postfix.get((r-cur) % p, 2*n) - i)
        postfix[cur] = i
    if min_len < n:
        return min_len
    return -1