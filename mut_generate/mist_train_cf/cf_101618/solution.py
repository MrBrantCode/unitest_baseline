"""
QUESTION:
Create three functions in Python: `kg_to_lb(weight)`, `lb_to_kg(weight)`, and `earth_to_moon(weight)`. The `kg_to_lb(weight)` function should take in a weight in kilograms and return the equivalent weight in pounds, using the formula `pounds = kilograms * 2.20462`. The `lb_to_kg(weight)` function should take in a weight in pounds and return the equivalent weight in kilograms, using the formula `kilograms = pounds / 2.20462`. The `earth_to_moon(weight)` function should take in the weight of an object in kilograms and return the weight in kilograms on the moon, using the formula `weight_on_moon = weight_on_earth * 0.165`.
"""

def kg_to_lb(weight):
    return weight * 2.20462

def lb_to_kg(weight):
    return weight / 2.20462

def earth_to_moon(weight):
    return weight * 0.165