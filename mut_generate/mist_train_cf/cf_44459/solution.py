"""
QUESTION:
Implement a function `min_difference(target, numbers)` that calculates the smallest attainable difference by deducting any possible combination of provided numbers from the target value. The function should take two parameters: `target` and `numbers`, where `target` is the explicitly denoted target value and `numbers` is a list of furnished digits. The function should return the smallest attainable difference.
"""

def min_difference(target, numbers):
    dp = [0] + [-1]*target
    for i in range(len(numbers)):
        for j in range(target, -1, -1):
            if dp[j] != -1 and j - numbers[i] >= 0:
                dp[j-numbers[i]] = max(dp[j-numbers[i]], dp[j] + numbers[i])
    min_diff = min([abs(i-dp[i]) for i in range(target+1) if dp[i] != -1])
    return min_diff