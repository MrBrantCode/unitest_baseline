"""
QUESTION:
Write a function `convert_temperatures` that takes a list of temperatures in Celsius as input and returns a dictionary with three keys: "converted_temperatures", "valid_count", and "invalid_count". The "converted_temperatures" key should map to a list of temperatures in Fahrenheit, with "Invalid temperature" for invalid inputs. The "valid_count" and "invalid_count" keys should map to the number of valid and invalid temperatures, respectively. A temperature is invalid if it is not a number or if it is below -273.15°C or above 1000°C. If the input list is empty, return "No temperature values provided".
"""

def convert_temperatures(temperatures):
    if not temperatures:
        return "No temperature values provided"

    converted_temperatures = []
    valid_count = 0
    invalid_count = 0

    for temperature in temperatures:
        if not isinstance(temperature, (int, float)):
            converted_temperatures.append("Invalid temperature")
            invalid_count += 1
        elif temperature < -273.15 or temperature > 1000:
            converted_temperatures.append("Invalid temperature")
            invalid_count += 1
        else:
            converted_temperature = (temperature * 9/5) + 32
            converted_temperatures.append(round(converted_temperature, 2))
            valid_count += 1

    response = {
        "converted_temperatures": converted_temperatures,
        "valid_count": valid_count,
        "invalid_count": invalid_count
    }

    return response