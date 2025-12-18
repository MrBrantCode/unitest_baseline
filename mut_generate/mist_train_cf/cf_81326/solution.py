"""
QUESTION:
Create a function named `calculate_compounded_interest` that takes in three parameters: the original principal amount `P`, the yearly nominal interest rate `r` (in decimal form), and the duration in years `t`. The function should return the final amount accumulated after `t` years, using the formula for continually compounded interest.
"""

import math

def calculate_compounded_interest(P, r, t):
    return P * math.exp(r * t)