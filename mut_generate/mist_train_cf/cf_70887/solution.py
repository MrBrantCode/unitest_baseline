"""
QUESTION:
Write a function named `countBalls` that takes two integers `lowLimit` and `highLimit` as input and returns the maximum number of balls that can be found in a single box. The box number is determined by the sum of the digits of a ball's number. The constraint is `1 <= lowLimit <= highLimit <= 10^5`.
"""

def countBalls(lowLimit: int, highLimit: int) -> int:
    from collections import defaultdict
    counts = defaultdict(int)
    for ball in range(lowLimit, highLimit+1):
        box = sum(int(digit) for digit in str(ball))
        counts[box] += 1
    return max(counts.values())