"""
QUESTION:
You are given an array `stones` of length `n`, where `3 <= n <= 10^4`, `1 <= stones[i] <= 10^9`, and all `stones[i]` are unique. `stones[i]` represents the location of the `i-th` pebble on a numerical line. Your goal is to shift the pebbles until they are in sequential positions by moving endpoint pebbles to vacant spots. Write a function `numMovesStonesII` to find the minimum and maximum number of moves required to achieve this.
"""

def numMovesStonesII(stones):
    stones.sort()
    i, n, low = 0, len(stones), len(stones)
    high = max(stones[-2] - stones[0], stones[-1] - stones[1]) - n + 2
    for j in range(n):
        while stones[j] - stones[i] >= n:
            i += 1
        if j - i + 1 == n - 1 and stones[j] - stones[i] == n - 2:
            low = min(low, 2)
        else:
            low = min(low, n - (j - i + 1))
    return [low, high]