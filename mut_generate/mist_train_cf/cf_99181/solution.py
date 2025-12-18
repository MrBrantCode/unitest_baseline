"""
QUESTION:
Create a function `relative_moisture_level` that takes three arguments - `saturated_weight`, `dry_weight`, and `current_weight`, and returns the relative moisture level as a percentage. The relative moisture level is calculated using the formula: `((current_weight - dry_weight) / (saturated_weight - dry_weight)) * 100`. The function should not take any other arguments.
"""

def relative_moisture_level(saturated_weight, dry_weight, current_weight):
    return ((current_weight - dry_weight) / (saturated_weight - dry_weight)) * 100