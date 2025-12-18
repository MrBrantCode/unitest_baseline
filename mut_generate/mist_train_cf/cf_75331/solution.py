"""
QUESTION:
Given a list of unique age variances in a population cluster, write a function `calculate_mean_age` that takes the list of ages as input and returns the numerical mean age. The function should calculate the mean by dividing the sum of all ages by the total number of ages.
"""

def calculate_mean_age(ages):
    return sum(ages)/len(ages)