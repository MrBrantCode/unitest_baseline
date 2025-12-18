"""
QUESTION:
Create a function `warmer_temperatures(temperatures: List[int]) -> List[int]` that takes a list of integers representing temperatures and returns a list of integers representing the number of days until a warmer temperature is encountered for each day. If there is no such day, the value should be set to 0.
"""

from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = []
    res = [0] * len(temperatures)
    
    for i, n in enumerate(temperatures):
        while stack and n > temperatures[stack[-1]]:
            last = stack.pop()
            res[last] = i - last
        stack.append(i)
    
    return res