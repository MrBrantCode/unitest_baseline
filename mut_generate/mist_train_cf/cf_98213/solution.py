"""
QUESTION:
Write a function `calculate_penalty` that calculates a penalty for submitting work late based on the number of days late, importance factor, extenuating circumstances factor, and base penalty. The function should take four arguments: `days_late`, `importance_factor`, `ext_circumstances_factor`, and `base_penalty`, and return the calculated penalty.
"""

def calculate_penalty(days_late, importance_factor, ext_circumstances_factor, base_penalty):
    penalty = days_late * importance_factor * ext_circumstances_factor * base_penalty
    return penalty