"""
QUESTION:
Write a function named `choose_num` that takes four positive integers `x`, `y`, `z`, and `w` as inputs. The function should return the largest even number within the range `[x, y]` (including `x` and `y`) that can be divided by both `z` and `w`. If no such number exists within the specified range, the function should return -1. Assume that `x` and `y` may be in any order. The function should validate the input types and values, and return an error message if they are invalid.
"""

def choose_num(x, y, z, w):
    """
    This function takes four positive integers x, y, z and w as inputs. It determines and returns the largest even number within the range [x, y] (including x and y) that can be divided by both z and w. If no such number exists within the specified range, the function should return -1.
    """
    # check if inputs are valid
    if not (isinstance(x, int) and isinstance(y, int) and x > 0 and y > 0 and z > 0 and w > 0):
        return "Invalid inputs, please enter positive integers."

    # switch x and y if x is greater than y
    if x > y:
        x, y = y, x

    # ensure y starts from an even number
    if y % 2 != 0:
        y -= 1

    for i in range(y, x-1, -2):
        if i % z == 0 and i % w == 0:
            return i

    return -1