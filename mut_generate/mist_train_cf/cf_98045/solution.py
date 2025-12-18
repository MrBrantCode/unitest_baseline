"""
QUESTION:
Create a function called `group_by_age` that takes a list of tuples as input, where each tuple contains a person's name and age. The function should return a dictionary where the keys are unique ages and the values are lists of names of people who have that age. If the input list is empty or contains tuples with invalid data types for name or age, the function should return an empty dictionary and print an error message. The function should also sort the names within each age group alphabetically. Assume that each name is a string of alphanumeric characters and each age is a positive integer.
"""

def group_by_age(people):
    # Check if input is empty
    if not people:
        print("Input list is empty.")
        return {}

    # Initialize an empty dictionary to store the results
    result = {}

    # Iterate through the list of tuples and group the people by age
    for name, age in people:
        # Check if name or age is of invalid data type
        if not isinstance(name, str) or not isinstance(age, int) or age <= 0:
            print("Invalid data type for name or age.")
            return {}

        if age in result:
            result[age].append(name)
        else:
            result[age] = [name]

    # Sort the names within each age group alphabetically
    for age in result:
        result[age].sort()

    return result