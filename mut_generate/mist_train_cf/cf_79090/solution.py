"""
QUESTION:
Calculate the probability that exactly two out of four 20-sided dice will display an even number when rolled. The dice are fair and each die has faces distinctly numbered from 1 to 20. The function name should be `combinations`.
"""

import math

def combinations(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def calculate_probability():
    num_combinations = combinations(4, 2)
    probability_each_combination = (1/2)**4
    final_probability = num_combinations * probability_each_combination
    return final_probability

# Use combinations function for the problem, renamed the function as requested.
def entrance():
    return calculate_probability()

print(entrance())