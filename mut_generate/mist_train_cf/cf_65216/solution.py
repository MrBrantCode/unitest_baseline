"""
QUESTION:
Write a function `inputMask` that determines the input mask based on the length of the input string `capacity`. The function should return `InputMask.TON` if the length of `capacity` is greater than 3, otherwise return `InputMask.KG`. Assume that `InputMask.TON` and `InputMask.KG` are predefined constants. Note that `capacity` can be `null`.
"""

from enum import Enum

class InputMask(Enum):
    TON = 1
    KG = 2

def inputMask(capacity):
    if capacity is None:
        return InputMask.KG
    return InputMask.TON if len(capacity) > 3 else InputMask.KG