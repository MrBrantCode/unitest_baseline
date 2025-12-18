"""
QUESTION:
Write a function `calculate_total_weight` that takes two lists as input: `fruits` and `weights`. The function should calculate the total weight of the fruits that are both valid (i.e., they are one of "apple", "banana", "grape", "kiwi", "orange", or "pear") and have a weight of at least 100 grams. The function should return the total weight of these valid fruits.
"""

def calculate_total_weight(fruits, weights):
    total_weight = 0
    for i in range(len(fruits)):
        if fruits[i] in ["apple", "banana", "grape", "kiwi", "orange", "pear"] and weights[i] >= 100:
            total_weight += weights[i]
    return total_weight