"""
QUESTION:
Write a function `calculate_packages_needed` that takes in two parameters, `total_items` and `items_per_package`, and returns the minimum number of packages required to meet the total demand without exceeding it. The function should use the ceiling function from the math module to round up the division of `total_items` by `items_per_package`.
"""

import math

def calculate_packages_needed(total_items, items_per_package):
    return math.ceil(total_items / items_per_package)