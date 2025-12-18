"""
QUESTION:
You are given an integer array `nums` of even length `n` and integers `limit` and `k`, and a boolean array `canChange` of the same length as `nums`. `canChange[i]` is `true` if and only if `nums[i]` can be changed. The array `nums` is complementary if for all indices `i` (0-indexed), `nums[i] + nums[n - 1 - i]` equals the same number. Return the minimum number of moves required to make `nums` complementary such that the sum of all elements in `nums` is less than or equal to `k`. In one move, you can replace any integer from `nums` with another integer between `1` and `limit`, inclusive.

Constraints:
`n == nums.length`
`2 <= n <= 10^5`
`1 <= nums[i] <= limit <= 10^5`
`n` is even.
`1 <= k <= sum(nums)`
`canChange.length == n`
"""

def minMoves(nums, limit, k, canChange):
    n = len(nums)
    total_sum = sum(nums)
    changes = [0] * (limit * 2 + 2)

    for i in range(n // 2):
        s = nums[i] + nums[n - i - 1]
        min_val = min(nums[i], nums[n - i - 1])
        max_val = max(nums[i], nums[n - i - 1])
        if canChange[i] and canChange[n - i - 1]:
            changes[2] += 1
            changes[min_val + 1] -= 1
            changes[max_val + 1] -= 1
            changes[limit + min_val + 1] += 1
            changes[limit + max_val + 1] += 1
            changes[limit + s] -= 1
        elif canChange[i] or canChange[n - i - 1]:
            changes[s - min_val] += 1
            changes[s - max_val + 1] -= 1

    for i in range(1, len(changes)):
        changes[i] += changes[i - 1]

    left, right = 0, len(changes) - 1
    while left < right:
        mid = (left + right) // 2
        if total_sum - mid >= k:
            right = mid
        else:
            left = mid + 1

    return left