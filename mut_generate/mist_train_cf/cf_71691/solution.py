"""
QUESTION:
You are given the parameters `buckets`, `minutesToDie`, and `minutesToTest` and your task is to determine the least number of pigs required to identify the poisonous bucket within the given time frame. The constraints are: `1 <= buckets <= 1000`, `1 <= minutesToDie <= minutesToTest <= 100`. You need to create a function called `poorPiggies(buckets: int, minutesToDie: int, minutesToTest: int) -> int` to solve this problem.
"""

import math

def poorPiggies(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    return math.ceil(math.log(buckets)/math.log(minutesToTest//minutesToDie + 1))