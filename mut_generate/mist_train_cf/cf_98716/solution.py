"""
QUESTION:
Create a function called `alert_owner_and_count_stolen_goats` that takes a list of dictionaries representing animals, where each dictionary contains information about an animal's type, age, color, and whether it has been stolen. The function should alert the owner when a goat with a rare genetic mutation (represented by the color "White") is stolen and return the total count of stolen goats.
"""

def alert_owner_and_count_stolen_goats(animals):
    """
    Alerts the owner when a goat with a rare genetic mutation (represented by the color "White") is stolen and returns the total count of stolen goats.

    Args:
        animals (list): A list of dictionaries representing animals, where each dictionary contains information about an animal's type, age, color, and whether it has been stolen.

    Returns:
        int: The total count of stolen goats.
    """
    stolen_goats_count = 0

    for animal in animals:
        if animal["stolen"]:
            if animal["animal"] == "Goat" and animal["color"] == "White":
                print("ALERT: A rare genetic mutation goat has been stolen!")
            stolen_goats_count += 1

    return stolen_goats_count