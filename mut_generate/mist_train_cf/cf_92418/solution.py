"""
QUESTION:
Write a function named `fahrenheit_to_celsius` that takes a temperature in Fahrenheit as input and returns the equivalent temperature in Celsius without using any built-in temperature conversion functions or formulas. The function should handle numeric inputs.
"""

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius