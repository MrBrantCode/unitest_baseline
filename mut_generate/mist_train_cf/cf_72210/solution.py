"""
QUESTION:
Design a function `celsius_to_fahrenheit(celsius)` that takes a temperature in Celsius as input and returns the equivalent temperature in Fahrenheit, rounded to two decimal places. Design another function `fahrenheit_to_celsius(fahrenheit)` that takes a temperature in Fahrenheit as input and returns the equivalent temperature in Celsius, rounded to two decimal places. Additionally, design a third function `test_temperature_conversion()` that tests the accuracy of these conversion functions using edge cases and random test cases, and provide explanations for any failing tests. The conversion formulas are: Celsius to Fahrenheit: `(celsius_temperature * 9/5) + 32`, and Fahrenheit to Celsius: `(fahrenheit_temperature - 32) * 5/9`.
"""

def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)