"""
QUESTION:
Create a function `process_time_data` that takes in a list of time values and performs the following operations: conversion using a conversion factor, conversion between two different units, and forecasting using a specific method. The function should return a tuple containing three lists: the converted time values, the time values converted between units, and the forecasted time values. The function should have the following signature:
```python
def process_time_data(time_values: List[float]) -> Tuple[List[float], List[float], List[float]]:
```
"""

from typing import List, Tuple

def process_time_data(time_values: List[float]) -> Tuple[List[float], List[float], List[float]]:
    # Convert the time values using the conversion factor and time converter matrix
    converted_values = [value * 2 for value in time_values]
    
    # Convert the time values between two different units using a conversion function
    def bsw_to_wor(value: float) -> float:
        return value * 3
    
    converted_between_units = [bsw_to_wor(value) for value in time_values]
    
    # Generate a forecast for the time values using a specific forecasting method
    def wor_forecast(value: float) -> float:
        return value * 4
    
    forecasted_values = [wor_forecast(value) for value in time_values]
    
    return converted_values, converted_between_units, forecasted_values