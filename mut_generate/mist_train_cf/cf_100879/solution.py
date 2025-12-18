"""
QUESTION:
Create a function called `classify_plants` that takes a list of plant names as input and returns a dictionary where the keys are the plant names and the values are their corresponding classifications as either 'Gymnosperm' or 'Angiosperm'. The classification should be based on the plant's characteristics, where plants that produce seeds without flowers are classified as 'Gymnosperm' and plants that produce seeds enclosed in a fruit or flower are classified as 'Angiosperm'.
"""

def classify_plants(plant_names):
    """
    Classify plant names as 'Gymnosperm' or 'Angiosperm' based on their characteristics.

    Args:
        plant_names (list): List of plant names.

    Returns:
        dict: Dictionary with plant names as keys and their corresponding classifications as values.
    """
    classifications = {
        "Redwood tree": "Gymnosperm",
        "Maple tree": "Angiosperm",
        "Pine tree": "Gymnosperm",
        "Birch tree": "Angiosperm",
        "Oak tree": "Angiosperm"
    }
    classified_plants = {}
    for plant in plant_names:
        if plant in classifications:
            classified_plants[plant] = classifications[plant]
    return classified_plants