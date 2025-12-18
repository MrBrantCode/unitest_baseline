"""
QUESTION:
Implement a function `findMaxWithinIterations(arr, max_iterations)` that takes a list of integers and the maximum number of iterations allowed as input. The function should iteratively find the maximum value in the array within the specified number of iterations. If the maximum value is found within the iterations, return the maximum value; otherwise, return "No maximum found". The function should only iterate through the array for a maximum of `max_iterations` times.
"""

from typing import List, Union

def findMaxWithinIterations(arr: List[int], max_iterations: int) -> Union[int, str]:
    max_val = float('-inf')
    iterations = 0
    for num in arr:
        if num > max_val:
            max_val = num
        iterations += 1
        if iterations >= max_iterations:
            break
    if max_val == float('-inf'):
        return "No maximum found"
    return max_val