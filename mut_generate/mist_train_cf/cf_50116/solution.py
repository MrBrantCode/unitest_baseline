"""
QUESTION:
Write a function `tallestTower` that takes an array of integers `blocks` as input and returns the maximum possible height of a tower that can be constructed by splitting the blocks into two equal-height piles. The function should return 0 if the tower cannot be supported. The input array `blocks` will contain between 1 and 20 integers, each between 1 and 1000, and the sum of the integers will be less than or equal to 5000.
"""

def tallestTower(blocks):
    total = sum(blocks)
    dp = [0] * (total//2+1)
    for block in blocks:
        for i in range(total//2, block-1, -1):
            dp[i] = max(dp[i], dp[i-block] + block)
    return dp[total // 2] * 2 if dp[total // 2] * 2 == total else 0