"""
QUESTION:
Given an integer, return its base 7 string representation.

Example 1:

Input: 100
Output: "202"



Example 2:

Input: -7
Output: "-10"



Note:
The input will be in range of [-1e7, 1e7].
"""

def convert_to_base7(num: int) -> str:
    if num < 0:
        return '-' + convert_to_base7(-num)
    elif num < 7:
        return str(num)
    else:
        return convert_to_base7(num // 7) + str(num % 7)