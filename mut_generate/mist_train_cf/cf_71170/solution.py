"""
QUESTION:
Construct a function `compare_number_arrays_order(string1, string2)` to determine whether two input strings have identical arrays of unique numbers, disregarding non-digit elements and maintaining consistency with the order in which they appear. The function should consider decimal and negative numbers.
"""

import re

def compare_number_arrays_order(string1: str, string2: str):
    pattern = r"-?\d+\.\d+|-?\d+"
    list1 = [float(i) for i in list(re.findall(pattern, string1))]
    list2 = [float(i) for i in list(re.findall(pattern, string2))]
    
    return list1 == list2