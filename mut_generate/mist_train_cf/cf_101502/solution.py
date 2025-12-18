"""
QUESTION:
Write a function called `relative_moisture_level` that takes in the saturated weight, dry weight, and current weight of a soil sample and returns the relative moisture level as a percentage.
"""

def relative_moisture_level(saturated_weight, dry_weight, current_weight):
    return ((current_weight - dry_weight) / (saturated_weight - dry_weight)) * 100