"""
QUESTION:
Design a set of functions to convert temperatures between Fahrenheit, Celsius, and Kelvin scales. 

Create six functions: fahrenheit_to_celsius, fahrenheit_to_kelvin, celsius_to_fahrenheit, celsius_to_kelvin, kelvin_to_fahrenheit, and kelvin_to_celsius. Each function should take one temperature value as input and return the converted temperature.
"""

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def kelvin_to_celsius(k):
    return k - 273.15