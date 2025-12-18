"""
QUESTION:
Implement a function called `convert_temperature` that uses a recursive function to handle temperature conversions from Celsius to Fahrenheit. The function should only allow temperatures in the range of -273.15 to 1000 degrees Celsius, handle input errors, and display an error message if an invalid temperature is entered. For each input, the function should output the temperature in Fahrenheit if it's above freezing (0 degrees Celsius), otherwise output "It is too cold". Additionally, the function should keep track of and display the highest and lowest temperature encountered after each input.
"""

def convert_temperature(celsius_temp):
    """
    This function converts temperature from Celsius to Fahrenheit, checks if it's above freezing,
    and returns the result along with the highest and lowest temperatures encountered.

    Args:
        celsius_temp (float): The temperature in Celsius.

    Returns:
        tuple: A tuple containing a string with the temperature in Fahrenheit (or "It is too cold" if below freezing)
               and a tuple with the highest and lowest temperatures encountered.
    """

    # Initialize highest and lowest temperatures
    if not hasattr(convert_temperature, 'highest_temp'):
        convert_temperature.highest_temp = -273.15
        convert_temperature.lowest_temp = 1000

    # Check if temperature is within valid range
    if celsius_temp < -273.15 or celsius_temp > 1000:
        return "Invalid temperature entered. Please enter a temperature in the range of -273.15 to 1000 degrees Celsius.", (convert_temperature.highest_temp, convert_temperature.lowest_temp)

    # Convert to Fahrenheit
    fahrenheit_temp = (celsius_temp * 9/5) + 32

    # Check if temperature is above freezing
    if celsius_temp > 0:
        result = "Temperature in Fahrenheit: {:.2f}".format(fahrenheit_temp)
    else:
        result = "It is too cold."

    # Update highest and lowest temperatures
    convert_temperature.highest_temp = max(convert_temperature.highest_temp, celsius_temp)
    convert_temperature.lowest_temp = min(convert_temperature.lowest_temp, celsius_temp)

    return result, (convert_temperature.highest_temp, convert_temperature.lowest_temp)