"""
QUESTION:
Given a mixed array of number and string representations of integers, add up the string integers and subtract this from the total of the non-string integers. 

Return as a number.
"""

def calculate_mixed_array_difference(lst):
    return sum((n if isinstance(n, int) else -int(n) for n in lst))