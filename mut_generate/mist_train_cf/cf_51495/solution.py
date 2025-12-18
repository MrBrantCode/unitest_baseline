"""
QUESTION:
Write a function `tallestBillboard(rods)` that takes an array of integers `rods` as input, representing the lengths of rods that can be fused together to form the supports of a billboard. The function should return the maximum feasible height for the billboard installation, where the two supports must be of identical height. If the billboard cannot be supported, return 0.

The input array `rods` has the following constraints: `1 <= len(rods) <= 20`, `1 <= rods[i] <= 1000`, and `sum(rods[i]) <= 5000`.
"""

def tallestBillboard(rods):
    sum_ = sum(rods)
    dp = [0] + [-10000] * sum_
    for x in rods:
        dp = [max(dp[i], dp[i-x] + x) if i >= x else dp[i] for i in range(sum_+1)]
    return dp[sum_//2]