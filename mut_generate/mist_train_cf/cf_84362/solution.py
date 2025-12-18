"""
QUESTION:
Create a function `average_numbers` that takes two lists as input: a list of strings and a list of lists containing elements of different types. The function should return a dictionary where the keys are the strings from the first list and the values are the average of the numerical elements in the corresponding sublist from the second list, ignoring non-numerical values.
"""

from typing import List, Union
from numbers import Number

def average_numbers(list1: List[str], list2: List[List[Union[Number, str]]]) -> dict:
    return {k: sum(v)/len(v) if v else 0 for k,v in zip(list1, [[n for n in sublist if isinstance(n, Number)] for sublist in list2])}