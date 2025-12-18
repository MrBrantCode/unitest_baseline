"""
QUESTION:
Write a function named `fahrenheit_to_celsius` that takes one argument, the temperature in Fahrenheit, and returns the temperature converted to Celsius. The function should not use any built-in temperature conversion functions or formulas.
"""

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius