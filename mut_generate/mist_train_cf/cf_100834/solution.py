"""
QUESTION:
Write a function `solution_y` that takes a non-negative integer `x` as input, where `x` lies within the interval [0,20], and returns a non-negative integer `y` such that the equation `4x - 7y + 9 = 0` is satisfied and `y` is not divisible by 3.
"""

def solution_y(x):
    y = (4*x + 9)//7  
    if y % 3 == 0:
        for k in (1, -1):
            if (4*x + 9 + k) % 7 != 0:
                y = (4*x + 9 + k)//7
                break
    return y