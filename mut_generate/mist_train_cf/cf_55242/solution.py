"""
QUESTION:
Create a function named `convert_to_fahrenheit` that takes a list of temperatures in Celsius as input and returns a list of temperatures in Fahrenheit. The function should handle invalid inputs, including non-numerical data and temperatures below absolute zero (-273.15°C), and append corresponding error messages to the output list instead of the converted temperature.
"""

def convert_to_fahrenheit(temp_list):
    ABSOLUTE_ZERO_CELSIUS = -273.15
    converted_temps = []
    
    for temp in temp_list:
        try:
            temp_celsius = float(temp)
            if temp_celsius < ABSOLUTE_ZERO_CELSIUS:
                 converted_temps.append("Invalid temperature below absolute zero")
            else:
                temp_fahrenheit = temp_celsius * 9/5 + 32
                converted_temps.append(temp_fahrenheit)
        except ValueError:
            converted_temps.append("Invalid input, not a number")
            
    return converted_temps