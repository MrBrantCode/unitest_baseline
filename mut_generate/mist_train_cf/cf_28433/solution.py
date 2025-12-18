"""
QUESTION:
Implement a function `calculate_rmse` that takes two lists of numeric values `a` and `b` as input, and returns the Root Mean Squared Error (RMSE) value. The function should calculate the RMSE using the formula: RMSE = sqrt(mean((a - b)^2)). If the input lists `a` and `b` are of different lengths, the function should return an error message.
"""

from typing import List, Union
import math

def calculate_rmse(a: List[float], b: List[float]) -> Union[float, str]:
    if len(a) != len(b):
        return "Input lists must be of the same length"
    
    squared_diff = [(a[i] - b[i])**2 for i in range(len(a))]
    mean_squared_diff = sum(squared_diff) / len(a)
    rmse = math.sqrt(mean_squared_diff)
    
    return rmse