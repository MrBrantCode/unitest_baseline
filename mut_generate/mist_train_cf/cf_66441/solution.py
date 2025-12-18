"""
QUESTION:
Write a function `ternary_operator_solution(x, y)` that takes two arguments `x` and `y` and returns a string comparing their values. The function should handle cases where `x` or `y` are not numeric (either `int` or `float`) and return an error message in such cases. The comparison should result in one of three possible strings: "x is greater than y", "x is less than y", or "x is equal to y".
"""

def entrance(x, y):
    if type(x) not in (int, float) or type(y) not in (int, float):
        return "Invalid input. Please ensure x and y are numbers."

    result = "x is greater than y" if x > y else "x is less than y" if x < y else "x is equal to y"

    return result