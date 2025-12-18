"""
QUESTION:
Create a function `relative_moisture_level` that takes in three parameters: `saturated_weight`, `dry_weight`, and `current_weight`, and returns the relative moisture level as a percentage using the formula `((current_weight - dry_weight) / (saturated_weight - dry_weight)) * 100`. The function should not take any other parameters or inputs.
"""

def relative_moisture_level(saturated_weight, dry_weight, current_weight):
    return ((current_weight - dry_weight) / (saturated_weight - dry_weight)) * 100