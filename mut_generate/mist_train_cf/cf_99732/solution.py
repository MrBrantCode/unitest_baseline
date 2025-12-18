"""
QUESTION:
Create a function called `relative_moisture_level` that calculates the relative moisture level of soil given the saturated weight, dry weight, and current weight of a soil sample. The function should return the relative moisture level as a percentage, calculated using the formula ((current_weight - dry_weight) / (saturated_weight - dry_weight)) * 100.
"""

def relative_moisture_level(saturated_weight, dry_weight, current_weight):
    return ((current_weight - dry_weight) / (saturated_weight - dry_weight)) * 100