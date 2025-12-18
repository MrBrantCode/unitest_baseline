"""
QUESTION:
You are given an integer array `nums` of even length `n` and an integer `limit`. In one move, you can replace any integer from `nums` with another integer between `1` and `limit`, inclusive. 

The array `nums` is complementary if for all indices `i` (0-indexed), `nums[i] + nums[n - 1 - i]` equals the same number. Given an integer `k`, find the minimum number of moves required to make `nums` complementary such that the sum of all elements in `nums` is less than or equal to `k`.
"""

def minMoves(nums, limit):
    n = len(nums)
    counts = {}
    total_sum = 0
    for i in range(n // 2):
        s = nums[i] + nums[n - 1 - i]
        total_sum += s
        if s not in counts:
            counts[s] = 1
        else:
            counts[s] += 1

    sorted_counts = sorted(counts.items())
    i = 0
    j = len(sorted_counts) - 1
    optimal = float('inf')
    while i <= j:
        X = sorted_counts[i][0]
        equal = sorted_counts[i][1]
        not_exceed = sorted_counts[i][1]
        for k in range(i + 1, j + 1):
            equal += sorted_counts[k][1]
            not_exceed += sorted_counts[k][1] * 2
        not_exceed += (X - 1) * equal
        if total_sum - equal * X + not_exceed <= limit:
            optimal = min(optimal, n - equal)
        else:
            diff = total_sum - equal * X + not_exceed - limit
            optimal = min(optimal, n - equal + (diff + X - 2) // (X - 1))
        i += 1
        if i <= j and sorted_counts[j][0] - sorted_counts[i][0] > 1:
            j -= 1

    return optimal