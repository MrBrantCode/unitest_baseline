"""
QUESTION:
Write a function called `uncycle` that takes a list of integers as input and returns the list in its original order after removing any cyclic shift. The function should use recursion to identify and remove the cyclic shift. The input list is guaranteed to be cyclically shifted in such a way that a simple binary search approach can be used to find the original order.

Function Signature: 
```python
def uncycle(list: List[int]) -> List[int]:
```

The input list is assumed to be a cyclically shifted version of a sorted list in ascending order. The function should return the original sorted list.
"""

from typing import List

def uncycle(list: List[int]) -> List[int]:
    if not list:
        return list
    min_index = list.index(min(list))
    return list[min_index:] + list[:min_index]