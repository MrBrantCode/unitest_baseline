"""
QUESTION:
Write a Python function called `calculate_probability` that calculates the probability of rolling two dice and achieving a sum greater than or equal to a given target sum. The function should take the target sum as an argument and return the calculated probability as a decimal value between 0 and 1.
"""

def calculate_probability(target_sum):
    favorable_outcomes = 0
    total_outcomes = 36

    for i in range(1, 7):
        for j in range(1, 7):
            if i + j >= target_sum:
                favorable_outcomes += 1

    return favorable_outcomes / total_outcomes