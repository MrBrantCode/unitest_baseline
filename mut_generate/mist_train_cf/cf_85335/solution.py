"""
QUESTION:
Write a Python function named `climate_data_extractor` that uses regular expressions to extract climate-related data from a given HTML text. The function should extract three types of data: carbon dioxide emission, temperature increase, and ice sheets loss. The function should return a tuple containing the extracted data. The HTML text is assumed to be in the format where the data appears as "X Y Z: number unit" (e.g., "Carbon Dioxide Emission: 40 Gt").
"""

import re

def climate_data_extractor(html_text):
    """
    Extracts climate-related data from the given HTML text using regular expressions.

    Args:
    html_text (str): The HTML text to extract data from.

    Returns:
    tuple: A tuple containing the extracted carbon dioxide emission, temperature increase, and ice sheets loss data.
    """

    # Define the patterns
    co2_pattern = r"([Cc]arbon\s[dD]ioxide\s[eE]mission).*?(\d.*?[\d\s]*[MGT]t*)"
    temperature_pattern = r"([Tt]emperature.*?increase).*?([\+\-]\d.*?°[CF])"
    ice_loss_pattern = r"([iI]ce\s[sS]heets\s[lL]oss).*?(\d.*?(km²|mi²))"

    # Find matches
    co2_matches = re.findall(co2_pattern, html_text)
    temperature_matches = re.findall(temperature_pattern, html_text)
    ice_loss_matches = re.findall(ice_loss_pattern, html_text)

    # Extract and return the data
    co2_data = co2_matches[0][1] if co2_matches else None
    temperature_data = temperature_matches[0][1] if temperature_matches else None
    ice_loss_data = ice_loss_matches[0][1] if ice_loss_matches else None

    return co2_data, temperature_data, ice_loss_data