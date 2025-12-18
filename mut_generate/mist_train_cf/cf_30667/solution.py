"""
QUESTION:
Write a function `warmer_days` that takes in an array of integers representing daily temperatures and returns an array of integers representing the number of days until the next warmer temperature. If there is no such day, the output should be 0.
"""

from typing import List

def warmer_days(temperatures: List[int]) -> List[int]:
    stack = []
    result = [0] * len(temperatures)
    
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    
    return result