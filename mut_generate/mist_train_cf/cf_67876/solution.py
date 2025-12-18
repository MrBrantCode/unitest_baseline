"""
QUESTION:
Write a function called `remove_duplicates` that takes a list of integers as input and returns a list of integers. The function should exclude all elements that appear more than once in the input list while maintaining the order of the remaining elements. The time complexity of the function should be O(n).
"""

from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    frequency_dict = {}
    output = []
    
    for number in numbers:
        if number in frequency_dict:
            frequency_dict[number] += 1
        else:
            frequency_dict[number] = 1
            output.append(number)
    
    return output