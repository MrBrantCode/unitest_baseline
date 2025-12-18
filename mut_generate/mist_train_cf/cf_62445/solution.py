"""
QUESTION:
Create a function called `convert_to_celsius` that takes in two parameters: `temp` and `original_scale`. The function should convert the given temperature from the specified scale to Celsius. The function should be able to handle temperatures in Fahrenheit, Kelvin, and Rankine scales. The function should also validate the input temperature to ensure it is within the valid range for the given scale. If the input is invalid, the function should return a message indicating the error. The valid temperature ranges are: Fahrenheit (-459.67 to infinity), Kelvin (0 to infinity), and Rankine (0 to infinity).
"""

def convert_to_celsius(temp, original_scale):
    """
    Converts a given temperature from the specified scale to Celsius.
    
    Args:
        temp (float): The temperature to be converted.
        original_scale (str): The original temperature scale. Can be 'Fahrenheit', 'Kelvin', or 'Rankine'.
    
    Returns:
        float: The temperature in Celsius. Returns an error message if the input is invalid.
    """
    
    # Validate the input temperature
    if original_scale.lower() == "fahrenheit":
        if temp < -459.67:
            return "Error: Temperature is below absolute zero (-459.67 degrees Fahrenheit)."
    elif original_scale.lower() == "kelvin":
        if temp < 0:
            return "Error: Temperature is below absolute zero (0 degrees Kelvin)."
    elif original_scale.lower() == "rankine":
        if temp < 0:
            return "Error: Temperature is below absolute zero (0 degrees Rankine)."
    else:
        return "Error: Invalid temperature scale."
    
    # Convert the temperature to Celsius
    if original_scale.lower() == "fahrenheit":
        return (temp - 32) * 5.0/9.0
    elif original_scale.lower() == "kelvin":
        return temp - 273.15
    elif original_scale.lower() == "rankine":
        return (temp - 491.67) * 5.0/9.0