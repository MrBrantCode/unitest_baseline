"""
QUESTION:
Develop a function named `compound_interest` that calculates the continuously compounded interest. The function should take three parameters: the initial sum `P`, the annual interest rate `r` (as a decimal), and the time `t` in years. The function should return the final amount after continuous compounding using the formula A = P * e^(rt).
"""

import math

def compound_interest(P, r, t):
  return P * math.exp(r * t)