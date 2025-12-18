"""
QUESTION:
Extract Climate Data

Write a function extract_climate_data that uses regular expressions to extract three values from a given string: global temperature rise in degrees Celsius, CO2 emissions in gigatonnes, and ice sheet loss in trillion tonnes. The function should return a dictionary with these values. 

Assume that the input string contains the values in the format specified by the following patterns:
- Global temperature rise: one or more digits followed by a dot and one or more digits, followed by " degrees Celsius global temperature rise"
- CO2 emissions: one or more digits followed by a dot and one or more digits, followed by " gigatonnes of CO2 emissions"
- Ice sheet loss: one or more digits followed by a dot and one or more digits, followed by " trillion tonnes of ice sheet loss"

Restrictions: The function should only use the re module for regular expressions and should not rely on any external libraries or modules.
"""

import re

def extract_climate_data(text):
    temp_pattern = re.compile(r'(\d+.\d+) degrees Celsius global temperature rise')
    co2_pattern = re.compile(r'(\d+.\d+) gigatonnes of CO2 emissions')
    ice_sheet_loss_pattern = re.compile(r'(\d+.\d+) trillion tonnes of ice sheet loss')

    temp_search = re.findall(temp_pattern, text)
    co2_search = re.findall(co2_pattern, text)
    ice_sheet_loss_search = re.findall(ice_sheet_loss_pattern, text)

    if temp_search and co2_search and ice_sheet_loss_search:
        return {
            'global_temperature_rise': float(temp_search[0]),
            'co2_emissions': float(co2_search[0]),
            'ice_sheet_loss': float(ice_sheet_loss_search[0])
        }
    else:
        return None