"""
QUESTION:
Write a function `min_stamps` that takes in a list of distinct postage stamp values and a target postal worth, and returns the minimum quantity of stamps necessary to achieve the target postal worth. The function should use a systematic and logical strategy, and consider potential anomalies and the impact of varying combinations of stamp values. The solution should balance computational efficiency and memory usage.
"""

def min_stamps(stamp_values, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for i in range(1, target + 1):
        for value in stamp_values:
            if value <= i:
                dp[i] = min(dp[i], dp[i - value] + 1)

    return dp[target] if dp[target] != float('inf') else -1