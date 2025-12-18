"""
QUESTION:
Create a data structure to store information about multiple individuals, including their name, age, weight, height, and gender. The data structure should be able to accommodate an arbitrary number of individuals.
"""

def create_individual_info(name, age, weight, height, gender):
    """
    Create a dictionary to store information about an individual.

    Args:
        name (str): The name of the individual.
        age (int): The age of the individual.
        weight (float): The weight of the individual.
        height (float): The height of the individual.
        gender (str): The gender of the individual.

    Returns:
        dict: A dictionary containing the individual's information.
    """
    return {
        "name": name,
        "age": age,
        "weight": weight,
        "height": height,
        "gender": gender
    }