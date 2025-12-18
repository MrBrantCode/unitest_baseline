"""
QUESTION:
Create a function `fahrenheit_converter` that takes a list of Celsius temperatures as input and returns a list of corresponding Fahrenheit temperatures. The conversion formula is (°F = (°C × 9/5) + 32). Use a lambda function and list comprehension to achieve this.
"""

def fahrenheit_converter(temperatures):
    return [((float(9)/5)*T + 32) for T in temperatures]