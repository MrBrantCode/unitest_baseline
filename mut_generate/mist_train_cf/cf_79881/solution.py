"""
QUESTION:
Given a list of integers `satisfaction` representing the satisfaction level of `n` dishes and an integer `k` representing the maximum number of dishes that can be discarded, write a function `maxSatisfaction(satisfaction, k)` that returns the maximum sum of Like-time coefficient that the chef can obtain after dishes preparation.

Constraints: `n == satisfaction.length`, `1 <= n <= 500`, `-10^3 <= satisfaction[i] <= 10^3`, `0 <= k <= n`.
"""

def maxSatisfaction(satisfaction, k):
    satisfaction.sort()
    tot, ans = 0, 0
    while satisfaction and satisfaction[-1] + tot > 0:
        tot += satisfaction.pop()  
        ans += tot
    while len(satisfaction) > k:
        removed_dish = satisfaction.pop(0)
        if tot - removed_dish > ans:
            tot -= removed_dish
            ans = tot
    return ans