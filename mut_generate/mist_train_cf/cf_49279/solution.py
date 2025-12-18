"""
QUESTION:
Create a function `dissect_number` that takes a float `num` and an optional boolean `round_down` as parameters, with `round_down` defaulting to `True`. The function should return a tuple containing the integer component and the decimal part of `num`, taking into account the rounding direction specified by `round_down`. The function should correctly handle negative values and ensure the decimal component is always between -1 and 1.
"""

import math
from typing import Tuple

def dissect_number(num: float, round_down: bool = True) -> Tuple[int, float]:
    if round_down:
        ipart = math.floor(num)
    else:
        ipart = math.ceil(num)
    
    decimals = abs(num - ipart)
    return (ipart, decimals)