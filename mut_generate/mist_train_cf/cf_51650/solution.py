"""
QUESTION:
Implement a selection algorithm and use it to estimate the median of a list of numbers. The selection algorithm should find the element at a given index in the sorted version of a list, without actually sorting the list. The median estimation function should handle tuples with negative and positive integers and decimals, and apply an optional multiplier. The function names are `selection_algorithm` and `advanced_median`. The `selection_algorithm` function takes a list of integers or floats and an index as input and returns the element at that index in the sorted version of the list. The `advanced_median` function takes a list of integers, floats, or tuples and an optional multiplier as input, applies the multiplier to the elements, and returns the median of the resulting list.
"""

from typing import List, Union

def entance(l: List[Union[int, float]], idx: int) -> float:
    if len(l) == 1:
        return l[0]

    pivot = l[len(l)//2]
    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if idx < len(lows):
        return entance(lows, idx)
    elif idx < (len(lows) + len(pivots)):
        return pivots[0]
    else:
        return entance(highs, idx - len(lows) - len(pivots))

def entance2(l: List[Union[int, float, tuple]], multiplier: float = 1.0) -> float:
    l = [el*multiplier if not isinstance(el, tuple) else el[0]*multiplier for el in l]

    if len(l) % 2 == 1:
        return entance(l, len(l) // 2)
    else:
        return 0.5 * (entance(l, len(l) // 2 - 1) +
                      entance(l, len(l) // 2))