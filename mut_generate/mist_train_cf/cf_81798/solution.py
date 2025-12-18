"""
QUESTION:
Write a function `canCross(stones, maxJump)` that determines if a frog can cross a river by landing on the last stone. The frog starts on the first stone and can only jump in the forward direction with the following rules: if the frog's last jump was `k` units, its next jump must be either `k - 1`, `k`, or `k + 1` units, but it cannot exceed the `maxJump`. The function should return `True` if the frog can reach the last stone and `False` otherwise.

The function should take two parameters: `stones`, a list of stone positions in sorted ascending order, and `maxJump`, the maximum jump length. The length of `stones` is between 2 and 2000, and `maxJump` is between 1 and 2^31 - 1. The first stone is always at position 0.
"""

def canCross(stones, maxJump):
    if stones[1] != 1:
        return False

    stone_positions = set(stones)
    dp = [set() for _ in range(len(stones))]
    dp[1].add(1)

    for i in range(2, len(stones)):
        for j in range(i):
            diff = stones[i] - stones[j]
            if diff-1 in dp[j] or diff in dp[j] or (diff+1 in dp[j] and diff+1 <= maxJump):
                dp[i].add(diff)
                if i == len(stones) - 1:
                    return True
    return False