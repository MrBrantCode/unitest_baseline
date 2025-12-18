"""
QUESTION:
Create a function `convert_temperature(temp, from_unit, to_unit)` that converts temperatures between Celsius, Fahrenheit, and Kelvin. The function should take a temperature value `temp` and the units `from_unit` and `to_unit` as parameters, and return the converted temperature. If `temp` is not a number, or if `from_unit` or `to_unit` is not 'Celsius', 'Fahrenheit', or 'Kelvin', the function should return an error message.
"""

def convert_temperature(temp, from_unit, to_unit):
    try:
        temp = float(temp)
    except ValueError:
        return "Invalid input: Temperature should be a number"

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    valid_units = ['celsius', 'fahrenheit', 'kelvin']

    if from_unit not in valid_units or to_unit not in valid_units:
        return "Invalid input: Unit must be 'Celsius', 'Fahrenheit', or 'Kelvin'"

    if from_unit == to_unit:
        # No conversion if both units are the same
        return temp

    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            # Celsius to Fahrenheit conversion
            return (temp * 9/5) + 32
        elif to_unit == 'kelvin':
            # Celsius to Kelvin conversion
            return temp + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            # Fahrenheit to Celsius conversion
            return (temp - 32) * 5/9
        elif to_unit == 'kelvin':
            # Fahrenheit to Kelvin conversion
            return ((temp - 32) * 5/9) + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            # Kelvin to Celsius conversion
            return temp - 273.15
        elif to_unit == 'fahrenheit':
            # Kelvin to Fahrenheit conversion
            return ((temp - 273.15) * 9/5) + 32