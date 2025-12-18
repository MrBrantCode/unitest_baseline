"""
QUESTION:
Create a function `survival_rate` that maps an `attack_rate` between 0 and 1 to a corresponding `survival_rate` between 0 and 1. The function should be such that a high `attack_rate` implies a low `survival_rate`. The `attack_rate` mostly assumes low values (<0.06), and the function should decay slowly for these values.
"""

import numpy as np

def survival_rate(attack_rate, k=30):
    return np.exp(-k * attack_rate)