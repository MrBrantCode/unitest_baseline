"""
QUESTION:
Write a function `calculateTotalMonths` that takes a list of durations with units ('year', 'month', or 'day') and returns the total duration in months. The function should assume each year has 12 months and each month has 30 days. The input list will not be empty and will only contain valid unit-duration pairs.
"""

from typing import List, Tuple, Union

def calculateTotalMonths(durations: List[Tuple[str, Union[int, float]]]) -> int:
    total_months = 0
    for unit, duration in durations:
        if unit == 'year':
            total_months += duration * 12
        elif unit == 'month':
            total_months += duration
        elif unit == 'day':
            total_months += duration / 30  # Assuming 30 days per month
    return int(total_months)