"""
QUESTION:
Define a function called `calculate_afternoon_species` to determine the number of bird species Keiko saw in the afternoon given two parameters: the total number of species she saw that day and the difference in the number of species she saw in the morning versus the afternoon. The function should return the number of species seen in the afternoon.
"""

def calculate_afternoon_species(total_species, additional_species):
    """
    Calculate the number of bird species Keiko saw in the afternoon.

    Args:
    total_species (int): The total number of species she saw that day.
    additional_species (int): The difference in the number of species she saw in the morning versus the afternoon.

    Returns:
    int: The number of species seen in the afternoon.
    """
    return (total_species - additional_species) // 2