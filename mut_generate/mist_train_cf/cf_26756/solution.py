"""
QUESTION:
Create a function `time_difference(a)` that calculates the time difference in minutes between two times in a 24-hour format. The input `a` is a list of four integers, where `a[0]` and `a[1]` represent the initial hour and minute, and `a[2]` and `a[3]` represent the final hour and minute. The function should consider the possibility that the final time might be on the next day.
"""

from typing import List

def time_difference(a: List[int]) -> int:
    start = 60 * a[0] + a[1]
    finish = 60 * a[2] + a[3]

    if finish <= start:
        finish += 1440  # 24 * 60 (adding 24 hours in minutes)

    time = finish - start
    return time