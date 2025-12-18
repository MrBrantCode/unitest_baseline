"""
QUESTION:
Create a function named `calculate_average_age` that takes a list of integers representing the ages of individuals in a population and returns their average age. The function should calculate the average by summing all the ages and dividing by the total number of individuals.
"""

def calculate_average_age(age_list):
    return sum(age_list) / len(age_list)