"""
QUESTION:
Implement a function `calculate_total_weight` that calculates the total weight of valid fruits from a given dictionary of fruits and their weights. A valid fruit is one that is in the list ['apple', 'banana', 'orange', 'mango', 'grape', 'kiwi', 'pineapple'] and has a weight of at least 100 grams. The total weight should exclude any fruits with a weight between 150 and 200 grams.
"""

def calculate_total_weight(fruits):
    total_weight = 0
    for fruit, weight in fruits.items():
        if fruit in ['apple', 'banana', 'orange', 'mango', 'grape', 'kiwi', 'pineapple'] and weight >= 100 and not 150 <= weight <= 200:
            total_weight += weight
    return total_weight