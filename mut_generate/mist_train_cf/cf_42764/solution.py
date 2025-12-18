"""
QUESTION:
Implement a function `calculate_total_time(reqs: List[int]) -> int` that takes a list of request processing times as input and returns the total time taken to process all the requests sequentially.
"""

from typing import List

def calculate_total_time(reqs: List[int]) -> int:
    total_time = 0
    for req in reqs:
        total_time += req
    return total_time