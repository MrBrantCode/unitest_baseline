"""
QUESTION:
Write a function `calculate_correlation(x, y)` that calculates the correlation coefficient between two lists of integers `x` and `y`. The correlation coefficient should be rounded to 2 decimal places. The lists `x` and `y` have the same number of elements. The function should return a float value between -1 and 1.
"""

from typing import List
import math

def calculate_correlation(x: List[int], y: List[int]) -> float:
    n = len(x)
    sum_prod_x_y = sum([xi * yi for xi, yi in zip(x, y)])
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2

    sum_x_squared = sum([xi**2 for xi in x])
    sum_y_squared = sum([yi**2 for yi in y])

    numerator = n * sum_prod_x_y - sum_x * sum_y
    denominator = math.sqrt((n * sum_x_squared - squared_sum_x) * (n * sum_y_squared - squared_sum_y))

    correlation_coefficient = numerator / denominator
    return round(correlation_coefficient, 2)