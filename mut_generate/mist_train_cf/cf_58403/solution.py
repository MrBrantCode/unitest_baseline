"""
QUESTION:
Write a function `convert_temp` that takes two parameters: `temp` (a numeric temperature value) and `scale` (a string indicating the temperature scale). The function should return a tuple of two temperature values: the input temperature converted to the next two scales in the sequence (Fahrenheit -> Celsius -> Kelvin -> Fahrenheit). 

For example, if `scale` is 'F', the function should return the temperature in Celsius and Kelvin. If `scale` is 'C', the function should return the temperature in Fahrenheit and Kelvin, and so on. 

The `scale` parameter should be restricted to 'F', 'C', or 'K', and the function should return an error message if any other value is provided.
"""

def convert_temp(temp, scale):
    def Fahrenheit_to_Celsius(F):
        return (F-32) * 5.0/9.0

    def Celsius_to_Kelvin(C):
        return C + 273.15

    def Kelvin_to_Fahrenheit(K):
        return (K-273.15) * 9.0/5.0 + 32

    if scale.lower() == 'f':
        temp_celsius = Fahrenheit_to_Celsius(temp)
        return temp_celsius, Celsius_to_Kelvin(temp_celsius)
    elif scale.lower() == 'c':
        temp_kelvin = Celsius_to_Kelvin(temp)
        return Kelvin_to_Fahrenheit(temp_kelvin), temp_kelvin
    elif scale.lower() == 'k':
        temp_fahrenheit = Kelvin_to_Fahrenheit(temp)
        return temp_fahrenheit, Fahrenheit_to_Celsius(temp_fahrenheit)
    else:
        return "Invalid scale. Please enter F, C, or K."