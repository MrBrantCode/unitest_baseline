"""
QUESTION:
Create a function called `calculate_age_stats` that takes a 2D list of people where each sublist contains a person's name and age, and returns a dictionary containing the average, maximum, and minimum ages. The input list will always have at least two sublists (a header and at least one person). The first sublist is a header and should be ignored.
"""

def calculate_age_stats(people):
    """
    Calculate the average, maximum, and minimum ages from a 2D list of people.

    Args:
        people (list): A 2D list where each sublist contains a person's name and age.
                      The first sublist is a header and is ignored.

    Returns:
        dict: A dictionary containing the average, maximum, and minimum ages.
    """
    # Extract ages from the people list
    ages = [person[1] for person in people[1:]]

    # Calculate the average age
    average_age = sum(ages) / len(ages)

    # Find the maximum and minimum ages
    max_age = max(ages)
    min_age = min(ages)

    # Return the results as a dictionary
    return {
        "average_age": average_age,
        "max_age": max_age,
        "min_age": min_age
    }