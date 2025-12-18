"""
QUESTION:
Create a function `reorganize_ages` that takes a dictionary where the keys are names and the values are lists of ages. Return a new dictionary where the keys are the ages and the values are lists of names. The function should allow for efficient retrieval of names based on age and handle duplicate age values.
"""

def reorganize_ages(people):
    """
    Reorganize a dictionary where the keys are names and the values are lists of ages
    into a new dictionary where the keys are the ages and the values are lists of names.

    Args:
        people (dict): A dictionary where the keys are names and the values are lists of ages.

    Returns:
        dict: A dictionary where the keys are the ages and the values are lists of names.
    """

    # Initialize an empty dictionary to store the reorganized data
    ages = {}

    # Iterate over each person in the input dictionary
    for person, age_list in people.items():
        # Iterate over each age associated with the person
        for age in age_list:
            # If the age is not already a key in the ages dictionary, add it with an empty list as its value
            if age not in ages:
                ages[age] = []
            # Add the person's name to the list of names associated with their age
            ages[age].append(person)

    # Return the reorganized dictionary
    return ages