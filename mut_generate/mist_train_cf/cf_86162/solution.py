"""
QUESTION:
Write a function `five_div_seq` that takes three integers `n`, `start`, and `end` as input. The function should generate a unidirectional decrementing arithmetic progression from `start` to `end`, filter out integers that are greater than or equal to `n` or not divisible by either 9 or 14, and count the occurrences of the digit '5' in the remaining integers. The function should return the total count of '5'.
"""

def five_div_seq(n: int, start: int, end: int) -> int:
    return sum(str(i).count('5') for i in range(start, end-1, -1) if i < n and (i % 9 == 0 or i % 14 == 0))