"""
QUESTION:
Implement the `add_compound_to_media` function in the `MediaManager` class. The function should add a compound to the `media` dictionary. If a component (`cmp`) is provided, append it to the compound's ID with an underscore in between. The compound's ID (with or without the component) should be used as the key in the `media` dictionary, and its lower and upper bounds should be stored as a tuple.
"""

def add_compound_to_media(media, compound, cmp=None):
    """
    Add a compound to the media dictionary.
    
    Args:
    media (dict): The media dictionary to add the compound to.
    compound (Compound): The compound to add.
    cmp (str, optional): The component to append to the compound ID. Defaults to None.
    
    Returns:
    dict: The updated media dictionary.
    """
    met_id = compound.id
    if cmp is not None:
        met_id += '_' + cmp
    media[met_id] = (compound.lower_bound, compound.upper_bound)
    return media