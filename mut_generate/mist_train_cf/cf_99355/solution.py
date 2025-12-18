"""
QUESTION:
Write a Python function named `convert_weight` that takes a weight in kilograms as input and returns the weight in grams (rounded to the nearest hundredth decimal place), pounds, and ounces. The function should use the conversion factors 1 kilogram = 1000 grams, 1 kilogram = 2.20462 pounds, and 1 pound = 16 ounces.
"""

def convert_weight(weight_in_kgs):
    weight_in_grams = round(weight_in_kgs * 1000, 2)
    weight_in_pounds = round(weight_in_kgs * 2.20462, 2)
    weight_in_ounces = round(weight_in_pounds * 16, 2)
    return weight_in_grams, weight_in_pounds, weight_in_ounces