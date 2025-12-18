"""
QUESTION:
Write a function called solution_y that takes an integer x as input, where 0 ≤ x ≤ 20, and returns the corresponding integer y that satisfies the equation 4x - 7y + 9 = 0. The function should return an integer y if it exists and is within the interval [0, 20]; otherwise, it should return None.
"""

def solution_y(x):
    numerator = 4 * x + 9
    if numerator % 7 == 0:
        y = numerator // 7
        if 0 <= y <= 20:
            return y
    return None