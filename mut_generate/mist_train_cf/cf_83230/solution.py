"""
QUESTION:
Create a function `fahrenheit_to_celsius` that takes a temperature in Fahrenheit as input and returns the equivalent temperature in Celsius. The conversion should use the formula Celsius = (Fahrenheit - 32) * 5/9. The function should support floating-point arithmetic to ensure accurate results.
"""

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius