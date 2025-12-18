"""
QUESTION:
Write a function named `convert_weight` that takes a weight in kilograms as input and returns its equivalent in grams, pounds, and ounces. The function should round the result to the nearest hundredth decimal place.
"""

def convert_weight(weight_in_kgs):
    weight_in_grams = round(weight_in_kgs * 1000, 2)
    weight_in_pounds = round(weight_in_kgs * 2.20462, 2)
    weight_in_ounces = round(weight_in_pounds * 16, 2)
    
    return weight_in_grams, weight_in_pounds, weight_in_ounces