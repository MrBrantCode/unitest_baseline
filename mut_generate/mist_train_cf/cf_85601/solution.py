"""
QUESTION:
Create a function `advanced_median` that calculates the median of a list of integers, floats, and tuples with a single float value, without sorting the list or using library functions. The function should handle negative and positive numbers, and decimals. It should also apply an optional multiplier to the values. The function should return the calculated median as a float. The list can contain duplicate values. The multiplier is a float with a default value of 1.0.
"""

from typing import List, Union

def advanced_median(l: List[Union[int, float, tuple]], multiplier: float = 1.0) -> float:
    """Estimates the median of constituents in the list 'l' without sorting them or using library function.
    Handles tuples with negative and positive integers, and decimals, with the use of an optional multiplier.
    """
    def selection_algorithm(sublist: List[Union[int, float]], idx: int) -> float:
        """A simple selection algorithm that finds the element at index `idx` in the sorted version of `sublist`, without actually sorting sublist."""
        if len(sublist) == 1:
             return sublist[0]

        pivot = sublist[len(sublist) // 2]
        lows = [el for el in sublist if el < pivot]
        highs = [el for el in sublist if el > pivot]
        pivots = [el for el in sublist if el == pivot]

        if idx < len(lows):
            return selection_algorithm(lows, idx)
        elif idx < len(lows) + len(pivots):
            return pivots[0]
        else:
            return selection_algorithm(highs, idx - len(lows) - len(pivots))

    # unwrap tuples and apply multiplier
    l = [el * multiplier if not isinstance(el, tuple) else el[0]*multiplier for el in l]

    if len(l) % 2 == 1:
        return selection_algorithm(l, len(l) // 2)
    else:
        return 0.5 * (selection_algorithm(l, len(l) // 2 - 1) +
                      selection_algorithm(l, len(l) // 2))