"""
QUESTION:
Create a function named `filter_and_convert_temps` that accepts a list of Kelvin temperatures and a Fahrenheit threshold as inputs. The function should convert each Kelvin temperature to Fahrenheit, filter out any temperature above the Fahrenheit threshold, and return a sorted list of the remaining temperatures. The function should handle non-numeric input. The conversion formula is (K − 273.15) * 9/5 + 32.
"""

def filter_and_convert_temps(kelvin_temps, fahrenheit_threshold):
    try:
        fahrenheit_temps = [(temp - 273.15) * 9/5 + 32 for temp in kelvin_temps]
        return sorted([temp for temp in fahrenheit_temps if temp <= fahrenheit_threshold])
    except TypeError:
        return "Error: All elements in the list must be numeric."