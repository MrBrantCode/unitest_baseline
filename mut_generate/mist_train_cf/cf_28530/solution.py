"""
QUESTION:
Implement a function `get_packed_values(integers, format_type)` that takes a list of integers and a format type as input and returns the corresponding packed values based on the given format type.

The function should handle two format types: "packed_U4" and "packed_I4". For "packed_U4", the packed value is the integer itself. For "packed_I4", the packed value is the integer itself for positive integers, and 256 plus the absolute value of the integer for negative integers.

Restrictions:
- The input list of integers has a length between 1 and 1000 (inclusive).
- Each integer in the list is between -128 and 127 (inclusive).
- The format type is either "packed_U4" or "packed_I4".
"""

from typing import List

def get_packed_values(integers: List[int], format_type: str) -> List[int]:
    if format_type == "packed_U4":
        return integers
    elif format_type == "packed_I4":
        return [num if num >= 0 else 256 + abs(num) for num in integers]