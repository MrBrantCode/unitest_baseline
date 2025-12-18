"""
QUESTION:
Given a list of probabilities where the index of each probability corresponds to the index of an outcome, write a function named `calculate_probability` that calculates the probability of an event occurring. The function should take two parameters: a list of probabilities and a list of indices of favourable outcomes. The function should return the final probability of the event occurring, considering that the total probability of all outcomes may not sum up to 1.
"""

def calculate_probability(probabilities, favourable_outcomes):
    total_probability = sum(probabilities)
    event_probability = sum([probabilities[i] for i in favourable_outcomes])
    final_probability = event_probability / total_probability
    return final_probability