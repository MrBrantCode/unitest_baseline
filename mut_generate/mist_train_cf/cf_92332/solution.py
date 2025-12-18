"""
QUESTION:
Write a function named `calculate_ages` that takes a 2D list as input where the first sublist contains the column headers "Person" and "Age", and the subsequent sublists contain the names and ages of individuals. The function should return the average age, maximum age, and minimum age of the individuals.
"""

def calculate_ages(people):
    # Extract ages from the people list
    ages = [person[1] for person in people[1:]]

    # Calculate the average age
    average_age = sum(ages) / len(ages)

    # Find the maximum and minimum ages
    max_age = max(ages)
    min_age = min(ages)

    # Return the average, maximum, and minimum ages
    return average_age, max_age, min_age