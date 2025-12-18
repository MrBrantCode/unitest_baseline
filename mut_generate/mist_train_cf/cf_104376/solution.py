"""
QUESTION:
Write a function `find_heavy_metal_fan` that determines which person among the given individuals listens to Heavy Metal, with the restriction that this person must also be a fan of Classic Rock. The input is a dictionary where keys are the names of people and values are their favorite music types, and the function must return the name of the person who listens to Heavy Metal and Classic Rock, or None if no such person exists.
"""

def find_heavy_metal_fan(favorites):
    """
    This function determines which person among the given individuals listens to Heavy Metal, 
    with the restriction that this person must also be a fan of Classic Rock.

    Args:
        favorites (dict): A dictionary where keys are the names of people and values are their favorite music types.

    Returns:
        str: The name of the person who listens to Heavy Metal and Classic Rock, or None if no such person exists.
    """
    for person, music in favorites.items():
        if music == "Classic Rock" and "Heavy Metal" in favorites.values():
            return person
    return None