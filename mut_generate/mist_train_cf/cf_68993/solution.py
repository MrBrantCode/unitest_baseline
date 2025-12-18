"""
QUESTION:
Calculate the additional quantity of each variety of juice needed to fill a 2-liter blender cup that already contains 0.8 liters of citrus orange fluid and 0.5 liters of tropical mango fluid. The function name should be `additional_juice_needed`.
"""

def additional_juice_needed(citrus_orange, tropical_mango, blender_volume):
    """
    Calculate the additional quantity of each variety of juice needed to fill a blender cup.

    Args:
    citrus_orange (float): The current volume of citrus orange juice in liters.
    tropical_mango (float): The current volume of tropical mango juice in liters.
    blender_volume (float): The total volume of the blender cup in liters.

    Returns:
    float: The additional quantity of juice needed to fill the blender cup.
    """
    current_total_volume = citrus_orange + tropical_mango
    additional_juice = blender_volume - current_total_volume
    return additional_juice