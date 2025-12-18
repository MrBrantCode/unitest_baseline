"""
QUESTION:
Create a function `relative_moisture_level` that calculates the relative moisture level of a soil sample given its saturated weight, dry weight, and current weight. The relative moisture level should be returned as a percentage.
"""

def relative_moisture_level(saturated_weight, dry_weight, current_weight):
    """Calculates the relative moisture level of a soil sample given its saturated weight, dry weight, and current weight."""
    return ((current_weight - dry_weight) / (saturated_weight - dry_weight)) * 100