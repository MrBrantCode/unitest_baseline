"""
QUESTION:
Implement a function `is_system_unhealthy` that takes a list of integers `health_measurements` and a positive integer `unhealthy_threshold` as input. The function should return `True` if the number of consecutive unhealthy measurements (represented by 0) exceeds or equals the `unhealthy_threshold`, and `False` otherwise.
"""

from typing import List

def is_system_unhealthy(health_measurements: List[int], unhealthy_threshold: int) -> bool:
    consecutive_unhealthy_count = 0
    for measurement in health_measurements:
        if measurement == 0:  
            consecutive_unhealthy_count += 1
            if consecutive_unhealthy_count >= unhealthy_threshold:
                return True
        else:
            consecutive_unhealthy_count = 0
    return False