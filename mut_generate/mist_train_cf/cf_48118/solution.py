"""
QUESTION:
Create a function "intersperse" that takes a list of integers and a delimiter integer, and returns a new list with the delimiter inserted between each pair of integers in the original list. The function should also have an optional boolean parameter "reverse" with a default value of False. If "reverse" is True, the original list should be reversed before inserting the delimiters.
"""

from typing import List

def intersperse(numbers: List[int], delimiter: int, reverse: bool = False) -> List[int]:
    if reverse:
        numbers = numbers[::-1]
        
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimiter)
    
    return result[:-1] if len(result) != 0 else []