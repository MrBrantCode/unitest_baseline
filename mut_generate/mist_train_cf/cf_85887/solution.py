"""
QUESTION:
Given a list of blocks where `blocks[i] = t` means the `i`-th block needs `t` units of time to be built, and the time cost of splitting one worker into two workers is `split`, find the minimum time needed to build all blocks with the constraint that workers can only split a maximum of `maxSplit` times.

Write a function `minBuildTime(blocks, split, maxSplit)` that takes in the list of blocks, the time cost of splitting, and the maximum number of splits as input and returns the minimum time required to build all blocks. The function should handle the constraints that `1 <= blocks.length <= 1000`, `1 <= blocks[i] <= 10^5`, `1 <= split <= 100`, and `1 <= maxSplit <= blocks.length`.
"""

import heapq

def minBuildTime(blocks, split, maxSplit):
    n = len(blocks)
    blocks.sort(reverse=True)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(n + 1):
            if j >= i:
                dp[i][j] = blocks[i]
            else:
                dp[i][j] = min(dp[i + 1][j] + blocks[i], dp[i][j + 1] + split)
    return min(dp[0][j] + j * split for j in range(maxSplit + 1))