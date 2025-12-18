"""
QUESTION:
Implement a function `generate_key_sequence(target_x, target_y)` that takes target coordinates `(target_x, target_y)` as input, assuming the character starts at the origin `(0, 0)` and can only move one unit at a time in any direction. The function should return a sequence of key presses ("U" for up, "D" for down, "L" for left, "R" for right) that will move the character to the target location efficiently, minimizing the number of key presses.
"""

def generate_key_sequence(target_x, target_y):
    key_sequence = ""
    if target_x > 0:
        key_sequence += "R" * target_x  # Press right key
    elif target_x < 0:
        key_sequence += "L" * abs(target_x)  # Press left key

    if target_y > 0:
        key_sequence += "U" * target_y  # Press up key
    elif target_y < 0:
        key_sequence += "D" * abs(target_y)  # Press down key

    return key_sequence