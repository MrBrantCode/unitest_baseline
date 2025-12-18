"""
QUESTION:
Create a function `convert_celsius` that takes a list of temperatures in Celsius as input and returns the corresponding temperatures in Fahrenheit. The input list is passed as a route parameter to a web service, and the output should be returned as a list of Fahrenheit temperatures. Use the formula (°C × 9/5) + 32 to convert Celsius to Fahrenheit.
"""

def convert_celsius(celsius):
    """
    This function takes a list of temperatures in Celsius, 
    converts them to Fahrenheit, and returns the result.

    Args:
        celsius (list): A list of temperatures in Celsius.

    Returns:
        list: A list of temperatures in Fahrenheit.
    """
    return [(temp * 9/5) + 32 for temp in celsius]