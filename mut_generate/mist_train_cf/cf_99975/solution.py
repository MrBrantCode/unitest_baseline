"""
QUESTION:
Create a function `relative_moisture_level(saturated_weight, dry_weight, current_weight)` that calculates the relative moisture level of a soil sample given its saturated weight, dry weight, and current weight. The relative moisture level should be calculated as a percentage using the formula: ((current_weight - dry_weight) / (saturated_weight - dry_weight)) * 100.
"""

def relative_moisture_level(saturated_weight, dry_weight, current_weight):
    """
    Calculates the relative moisture level of a soil sample given its saturated weight, dry weight, and current weight.

    Args:
        saturated_weight (float): The saturated weight of the soil sample.
        dry_weight (float): The dry weight of the soil sample.
        current_weight (float): The current weight of the soil sample.

    Returns:
        float: The relative moisture level as a percentage.
    """
    return ((current_weight - dry_weight) / (saturated_weight - dry_weight)) * 100