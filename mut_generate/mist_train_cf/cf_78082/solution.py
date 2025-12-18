"""
QUESTION:
Create a function "intersperse" that takes in a list of elements, a delimiter, and an optional boolean parameter "reverse" with a default value of False. If "reverse" is True, the function should reverse the list before performing the operation. The function should then insert the delimiter between each element in the list and return the resulting list. The delimiter should not be appended to the end of the list.
"""

from typing import List, Any

def intersperse(elements: List[Any], delimiter: Any, reverse: bool = False) -> List[Any]:
    if reverse:
        elements = elements[::-1]
    result = []
    for element in elements:
        result.append(element)
        result.append(delimiter)
    return result[:-1]