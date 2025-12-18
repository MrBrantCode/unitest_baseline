"""
QUESTION:
Create a function named `total_match` that takes two lists of alphanumeric strings and an optional boolean parameter `case_sensitive` with a default value of `False`. The function should return the list with the total character count (ignoring white spaces and non-alphanumeric characters) less than or equal to the other list's count, while preserving the original order of elements in each list. The function should also eliminate duplicate strings from both lists, keeping only the first occurrence of each string. If `case_sensitive` is `False`, the function should ignore text case during string evaluations; otherwise, it should be case sensitive. If both lists have an equal total character count, the function should return the first list.
"""

import re
from collections import OrderedDict

def total_match(lst1, lst2, case_sensitive=False):
    lst1 = [re.sub(r'\W+', '', s).lower() if not case_sensitive else re.sub(r'\W+', '', s) for s in lst1]
    lst2 = [re.sub(r'\W+', '', s).lower() if not case_sensitive else re.sub(r'\W+', '', s) for s in lst2]

    lst1, lst2 = list(OrderedDict.fromkeys(lst1)), list(OrderedDict.fromkeys(lst2))

    return lst1 if sum(len(s) for s in lst1) <= sum(len(s) for s in lst2) else lst2