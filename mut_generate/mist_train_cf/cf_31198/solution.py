"""
QUESTION:
Write a function `calculate_overall_rate(reactions: dict, reaction_set: set) -> float` that calculates the overall reaction rate for a given set of reactions. 

`reactions` is a dictionary where keys are reaction identifiers and values are tuples of the form `(direction, rate)` representing the direction and rate of the reaction. The direction can be "forward", "reverse", or "" (empty string) indicating a reversible reaction. 

`reaction_set` is a set of reaction identifiers for which the overall reaction rate needs to be calculated. 

The function should return the overall reaction rate as a floating-point number rounded to 4 decimal places. Assume that the reaction rates are non-negative and the reaction identifiers are unique within the given set of reactions.
"""

def entrance(reactions: dict, reaction_set: set) -> float:
    overall_rate = 1.0
    for reaction_id in reaction_set:
        direction, rate = reactions[reaction_id]
        if direction == "forward" or direction == "":
            overall_rate *= rate
        if direction == "reverse" or direction == "":
            overall_rate *= 1 / rate
    return round(overall_rate, 4)