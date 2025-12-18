"""
QUESTION:
Create a function `convert_temperatures` that takes a list of temperatures in Celsius as input. The function should convert the valid temperatures to Fahrenheit and return the converted temperatures along with the count of valid and invalid temperatures. A temperature is considered valid if it is within the range -273.15°C to 1000°C. If a temperature is invalid, it should be represented as "Invalid temperature" in the output. The function should handle both numeric and non-numeric inputs.
"""

def convert_temperatures(temperatures):
    """
    Converts a list of temperatures from Celsius to Fahrenheit, 
    handling valid and invalid temperatures.

    Args:
        temperatures (list): A list of temperatures in Celsius.

    Returns:
        tuple: A tuple containing the converted temperatures, 
               the count of valid temperatures, and the count of invalid temperatures.
    """

    def celsius_to_fahrenheit(temperature):
        return (temperature * 9/5) + 32

    def is_valid_temperature(temperature):
        return -273.15 <= temperature <= 1000

    valid_temperatures = []
    invalid_temperatures = []
    converted_temperatures = []

    for temperature in temperatures:
        if isinstance(temperature, (int, float)):
            if is_valid_temperature(temperature):
                valid_temperatures.append(temperature)
                converted_temperatures.append(round(celsius_to_fahrenheit(temperature), 1))
            else:
                invalid_temperatures.append(temperature)
                converted_temperatures.append("Invalid temperature")
        else:
            invalid_temperatures.append(temperature)
            converted_temperatures.append("Invalid temperature")

    return converted_temperatures, len(valid_temperatures), len(invalid_temperatures)