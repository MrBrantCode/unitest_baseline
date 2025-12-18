"""
QUESTION:
You are given an array of integers `stones` where `stones[i]` is the weight of the `ith` stone. The goal is to partition the stones into two groups such that the sum of weights in each group is as close as possible. Write a function `lastStoneWeightII` that returns the smallest possible weight of the left stone and the total number of smashes performed.

The function `lastStoneWeightII` should take an array of integers `stones` as input and return an array of two integers. The constraints are `1 <= stones.length <= 30` and `1 <= stones[i] <= 100`.
"""

def lastStoneWeightII(stones):
    total = sum(stones)
    dp = [False] * (total + 1)
    dp[0] = True
    cur_sum = 0
    
    for stone in stones:
        cur_sum += stone
        for i in range(cur_sum, stone - 1, -1):
            dp[i] = dp[i] or dp[i - stone]
    
    for i in range(total // 2, -1, -1):
        if dp[i]:
            return [total - 2 * i, len(stones) - 1]
    
    return [total, len(stones) - 1]