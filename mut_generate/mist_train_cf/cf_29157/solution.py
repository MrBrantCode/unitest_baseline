"""
QUESTION:
Implement a function `calculate_diastolic_stats(data: List[float]) -> Tuple[float, float]` that calculates the standard deviation and variability of a list of diastolic blood pressure readings. The function should take a list of float values as input and return a tuple containing the standard deviation and variability, both rounded to one decimal place. The standard deviation is a measure of the amount of variation or dispersion of the values, and the variability is the range between the maximum and minimum values. Handle edge cases such as empty input lists and lists with only one element, returning (0, 0) and (0, 0) respectively.
"""

from typing import List, Tuple
import statistics

def calculate_diastolic_stats(data: List[float]) -> Tuple[float, float]:
    if not data:
        return 0, 0  

    std_dev = statistics.stdev(data) if len(data) > 1 else 0  
    variability = max(data) - min(data)  

    return round(std_dev, 1), round(variability, 1)