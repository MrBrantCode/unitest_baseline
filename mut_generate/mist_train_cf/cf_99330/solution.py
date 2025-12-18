"""
QUESTION:
Write a function `calculate_penalty(days_late, importance_factor, ext_circumstances_factor, base_penalty)` that calculates the penalty for submitting work late. The function should take four parameters: the number of days late, the importance factor of the assignment, the extenuating circumstances factor, and the base penalty per day. The function should return the calculated penalty, which is the product of the four input parameters.
"""

def calculate_penalty(days_late, importance_factor, ext_circumstances_factor, base_penalty):
    penalty = days_late * importance_factor * ext_circumstances_factor * base_penalty
    return penalty