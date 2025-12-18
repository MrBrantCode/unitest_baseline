"""
QUESTION:
You have n dices each one having s sides numbered from 1 to s.
How many outcomes add up to a specified number k?

For example if we roll four normal six-sided dices we
have four outcomes that add up to 5. 

(1, 1, 1, 2)
(1, 1, 2, 1)
(1, 2, 1, 1)
(2, 1, 1, 1)
"""

def count_dice_outcomes(n: int, s: int, k: int) -> int:
    if n == 1:
        return 1 if 0 < k <= s else 0
    return sum((count_dice_outcomes(n - 1, s, k - j - 1) for j in range(s))) if k > 0 else 0