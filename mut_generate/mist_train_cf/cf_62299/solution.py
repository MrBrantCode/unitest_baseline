"""
QUESTION:
Write a function `danceOff(n: int, k: int)` that determines the winner of a dance-off where `n` participants are standing in a circle and every `kth` participant is eliminated, with the counting wrapping around the circle. The function should return the position of the winner (1-indexed). The input constraints are `1 <= k <= n <= 500`.
"""

def danceOff(n: int, k: int) -> int:
    if n == 1:
        return 0
    else:
        return (danceOff(n-1, k) + k) % n + 1