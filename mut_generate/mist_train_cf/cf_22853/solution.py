"""
QUESTION:
Create a function called `is_cyclic_rotation` that takes two non-negative integers `num1` and `num2` as input and returns a boolean indicating whether `num1` is a cyclic rotation of `num2`. A cyclic rotation is obtained by moving the last digit of a number to the first position and shifting all other digits one position to the right. The function should work for numbers of any length up to 10^6 digits and should be efficient in terms of both time and space complexity.
"""

def is_cyclic_rotation(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)

    if len(num1_str) != len(num2_str):
        return False

    cyclic_rotations = num1_str + num1_str

    return num2_str in cyclic_rotations