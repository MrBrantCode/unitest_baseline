"""
QUESTION:
Write a function `calculate_rectangle_properties` that takes the animation state `animation_state` and the value of `f` as input and returns the corresponding rectangle properties `left`, `top`, `right`, and `bottom` based on the given animation state and input values. The function should assume that `TS` is a predefined constant. For `animation_state` 4, calculate `left` as not explicitly set, `top` as `TS * 2`, `right` as `TS + (f * TS)`, and `bottom` as `(TS * 2) + TS`. For `animation_state` 5, calculate `left` as `f * TS`, `top` as `TS * 3`, `right` as `TS + (f * TS)`, and `bottom` as `(TS * 3) + TS`.
"""

from typing import Tuple

def calculate_rectangle_properties(animation_state: int, f: int, TS: int) -> Tuple[int, int, int, int]:
    if animation_state == 4:
        left = None  # Not explicitly set
        top = TS * 2
        right = TS + (f * TS)
        bottom = (TS * 2) + TS
    elif animation_state == 5:
        left = f * TS
        top = TS * 3
        right = TS + (f * TS)
        bottom = (TS * 3) + TS
    else:
        # Handle other animation states if needed
        left, top, right, bottom = None, 0, 0, 0  

    return left, top, right, bottom