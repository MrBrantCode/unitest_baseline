"""
QUESTION:
Write a function `process_s(s)` that takes a pandas Series `s` as input and performs the following operations:
- Returns a list containing the first element of the series `s`.
- Appends the first three elements of the series `s` to the list.
- Appends the elements of the series `s` that are greater than its median to the list.
- Appends the elements of the series `s` at indices 4, 3, and 1 to the list.
- Appends the exponentiation of the constant `e` raised to the power of each element in the series `s` to the list.

The function should return a list containing the results of the above operations in the order they are listed.
"""

import pandas as pd
import math

def process_s(s):
    results = []
    
    # Return the first element of the series s
    results.append(s.iloc[0])
    
    # Append the first three elements of the series s to the list
    results.append(s.iloc[:3].tolist())
    
    # Append the elements of the series s that are greater than its median to the list
    results.append(s[s > s.median()].tolist())
    
    # Append the elements of the series s at indices 4, 3, and 1 to the list
    results.append(s.iloc[[4, 3, 1]].tolist())
    
    # Append the exponentiation of the constant e raised to the power of each element in the series s to the list
    results.append([math.exp(val) for val in s])
    
    return results