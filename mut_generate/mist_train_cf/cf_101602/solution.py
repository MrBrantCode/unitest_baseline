"""
QUESTION:
Write a function `convert_weight` that takes a weight in kilograms as input and returns the weight in grams, pounds, and ounces. The weight in grams should be rounded to the nearest hundredth decimal place.
"""

def convert_weight(weight_in_kgs):
    weight_in_grams = weight_in_kgs * 1000
    weight_in_pounds = weight_in_kgs * 2.20462
    weight_in_ounces = weight_in_pounds * 16
    
    return {
        "grams": round(weight_in_grams, 2),
        "pounds": round(weight_in_pounds, 2),
        "ounces": round(weight_in_ounces, 2)
    }