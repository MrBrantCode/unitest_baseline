"""
QUESTION:
Create a function called `calculate_penalty` that calculates a penalty for submitting work late. The function should take in four parameters: `days_late`, `importance_factor`, `ext_circumstances_factor`, and `base_penalty`, which represent the number of days or hours the submission is late, the importance of the assignment (ranging from 0 to 1), the degree of extenuating circumstances (ranging from 0 to 1), and the fixed penalty amount per day or hour of late submission, respectively. The function should return the calculated penalty as the product of these four parameters.
"""

def calculate_penalty(days_late, importance_factor, ext_circumstances_factor, base_penalty):
    penalty = days_late * importance_factor * ext_circumstances_factor * base_penalty
    return penalty