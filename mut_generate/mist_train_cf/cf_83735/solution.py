"""
QUESTION:
Create a function `rolling_max` that takes two lists of integers `numbers1` and `numbers2` as input and returns a tuple of two lists. Each output list should contain the rolling maximum element found until the given moment in the sequence of the corresponding input list, along with the maximum value of each individual list. The function should handle cases where the input lists are empty.
"""

from typing import List, Tuple

def rolling_max(numbers1: List[int], numbers2: List[int]) -> Tuple[List[int], List[int]]:
    """From two given lists of integers, generate a list of rolling maximum element found until given moment 
    in the sequence and store them as maximum of each list.
    """
    if not numbers1 or not numbers2:
        return ([], [])

    max1 = numbers1[0]
    max2 = numbers2[0]
    
    rolling_max1 = [max1]
    rolling_max2 = [max2]
    
    for num in numbers1[1:]:
        if num > max1:
            max1 = num
        rolling_max1.append(max1)
        
    for num in numbers2[1:]:
        if num > max2:
            max2 = num
        rolling_max2.append(max2)
        
    return (rolling_max1, rolling_max2)