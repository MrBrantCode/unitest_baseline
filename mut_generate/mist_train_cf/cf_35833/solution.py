"""
QUESTION:
Implement the `calculateButtonSizeToFit` function, which takes a button's current size (`frame`) as a tuple of two integers representing the width and height, and a maximum allowed width (`maxWidth`) as an integer. The function should adjust the button's size to fit its content within the maximum width constraint and return the new size as a tuple of two integers representing the width and height. The function should not alter the height if possible.
"""

from typing import Tuple

def calculateButtonSizeToFit(frame: Tuple[int, int], maxWidth: int) -> Tuple[int, int]:
    if frame[0] <= maxWidth:
        return frame
    return (maxWidth, frame[1])