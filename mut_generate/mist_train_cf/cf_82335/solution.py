"""
QUESTION:
Determine the smallest possible number of rabbits that could inhabit a forest based on their responses regarding the number of other rabbits that share their color. Implement a function `minRabbits(answers)` where `answers` is an array of integers representing the responses of the rabbits. The length of `answers` will not exceed 1000 and each `answers[i]` will be an integer within the range `[0, 999]`.
"""

import collections
import math

def minRabbits(answers):
    response_counts = collections.Counter(answers)
    total = 0

    for response, count in response_counts.items():
        group_size = response + 1
        groups = math.ceil(count / group_size)
        total += groups * group_size

    return total