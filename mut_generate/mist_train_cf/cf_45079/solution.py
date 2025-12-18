"""
QUESTION:
Write a function `minMoves(nums, L, M)` that takes an integer array `nums`, and integers `L` and `M` as input. The function should return the minimum number of moves required to make all array elements equal, where in one move you can either increment `n - 1` elements of the array by `1` or decrement `1` element of the array by `1`, with the constraint that no element can exceed `L` or go below `M`. If it's impossible to make all elements equal without breaking the limit, return `-1`.

Constraints: `1 <= len(nums) <= 10^4`, `-10^9 <= nums[i], L, M <= 10^9`.
"""

def minMoves(nums, L, M):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = 0

    for num in nums:
        diff = abs(num - median)
        if (num + diff <= L and num + diff >= M) or (num - diff <= L and num - diff >= M):
            moves += diff
        else:
            return -1

    return moves