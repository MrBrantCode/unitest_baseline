"""
QUESTION:
Create a function called `calculate_sum` that takes an array of float values as input, returns the sum of all elements between 0 and 100 inclusive, rounded to two decimal places, and is efficient for arrays with up to 10^6 elements.
"""

def calculate_sum(array):
    total = 0.0
    for value in array:
        if value >= 0 and value <= 100:
            total += value
    return round(total, 2)