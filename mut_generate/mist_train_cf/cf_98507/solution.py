"""
QUESTION:
Write a function called solution_y that takes an integer x as input and returns a corresponding integer y that satisfies the equation 4x - 7y + 9 = 0, where x and y are non-negative integers within the interval [0,20] and y is not divisible by 3.
"""

def solution_y(x):
    y = (4*x + 9)//7  # integer division to get integer result
    if y % 3 == 0:
        for k in (1, -1):
            if (4*x + 9 + k) % 7 != 0:
                y = (4*x + 9 + k)//7
                break
    return y