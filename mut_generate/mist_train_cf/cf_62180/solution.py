"""
QUESTION:
Create a Python function `mine_environmental_data` that takes a string representing the HTML content of a webpage as input and returns a dictionary containing three lists of matched values: 'temperature', 'co2', and 'polar_ice'. The function should use regular expressions to extract data in the format of temperature measurements in degrees, carbon dioxide output in parts per million (ppm), and polar ice deterioration in square kilometers (km²).
"""

import re

def mine_environmental_data(html_content):
    """
    Extracts temperature, CO2, and polar ice data from the given HTML content.

    Args:
        html_content (str): The HTML content of a webpage.

    Returns:
        dict: A dictionary containing three lists of matched values: 'temperature', 'co2', and 'polar_ice'.
    """

    # Define regex patterns
    temperature_pattern = r'([+-]?[0-9]*[.]?[0-9]+) degree'  # E.g., matches "2.5 degree"
    co2_pattern = r'([+-]?[0-9]*[.]?[0-9]+) ppm'  # E.g., matches "400 ppm"
    polar_ice_pattern = r'([+-]?[0-9]*[.]?[0-9]+) km²'  # E.g., matches "14.1 million km²"

    # Find matches
    temp_matches = re.findall(temperature_pattern, html_content)
    co2_matches = re.findall(co2_pattern, html_content)
    polar_ice_matches = re.findall(polar_ice_pattern, html_content)

    return {
        'temperature': temp_matches,
        'co2': co2_matches,
        'polar_ice': polar_ice_matches
    }