"""
QUESTION:
Implement a function named `calculate_frame_rate_type` that determines whether a variable or fixed frame rate is best for a given game scenario. The function should take in two parameters: `is_fluidity_priority` and `is_consistency_priority`, both of which are boolean values representing the priorities of the game. The function should return a string indicating whether a "variable" or "fixed" frame rate is recommended.
"""

def calculate_frame_rate_type(is_fluidity_priority, is_consistency_priority):
    """
    Determine whether a variable or fixed frame rate is best for a given game scenario.

    Parameters:
    is_fluidity_priority (bool): Whether fluidity is a priority for the game.
    is_consistency_priority (bool): Whether consistency is a priority for the game.

    Returns:
    str: "variable" or "fixed" indicating the recommended frame rate type.
    """
    if is_fluidity_priority and not is_consistency_priority:
        return "variable"
    elif is_consistency_priority and not is_fluidity_priority:
        return "fixed"
    elif is_fluidity_priority and is_consistency_priority:
        # In cases where both priorities are equal, variable frame rate is recommended
        return "variable"
    else:
        # If neither priority is set, default to fixed frame rate
        return "fixed"