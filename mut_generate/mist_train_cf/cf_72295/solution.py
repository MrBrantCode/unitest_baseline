"""
QUESTION:
Implement a Python function `fahrenheit_to_kelvin(f)` that takes a temperature in degrees Fahrenheit as input and returns the equivalent temperature in Kelvin, using the conversion formula `K = ((Fahrenheit – 32) * 5/9) + 273.15`.
"""

def fahrenheit_to_kelvin(f):
    k = ((f - 32) * (5/9)) + 273.15
    return k