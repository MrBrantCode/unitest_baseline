"""
QUESTION:
Write a function `is_cyclic_rotation(num1, num2)` that takes two non-negative integers `num1` and `num2` as input and returns `True` if `num1` is a cyclic rotation of `num2`, and `False` otherwise. The function should be efficient in terms of time and space complexity, handling numbers of up to 10^6 digits.
"""

def is_cyclic_rotation(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)

    if len(num1_str) != len(num2_str):
        return False

    cyclic_rotations = num1_str + num1_str

    if num2_str in cyclic_rotations:
        return True
    else:
        return False