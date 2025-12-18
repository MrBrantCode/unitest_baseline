"""
QUESTION:
Create a function `celsius_to_fahrenheit(temperatures)` that takes a list of temperatures in Celsius as input, where temperatures can be integers, floats, or invalid inputs (non-numeric values or temperatures below -273.15°C). The function should return a list of converted temperatures in Fahrenheit, replacing invalid temperatures with "Invalid temperature", along with the total count of valid and invalid temperatures. The function should be able to handle a mix of valid and invalid temperature values in the input list.
"""

def celsius_to_fahrenheit(temperatures):
    valid_temperatures = []
    invalid_count = 0
    
    for temperature in temperatures:
        if isinstance(temperature, (int, float)):
            if temperature < -273.15:
                valid_temperatures.append("Invalid temperature")
                invalid_count += 1
            else:
                valid_temperatures.append(round((temperature * 9/5) + 32, 1))
        else:
            valid_temperatures.append("Invalid temperature")
            invalid_count += 1
    
    return {
        "converted_temperatures": valid_temperatures,
        "valid_count": len(valid_temperatures) - invalid_count,
        "invalid_count": invalid_count
    }