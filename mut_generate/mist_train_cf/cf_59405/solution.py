"""
QUESTION:
Write a function `extract_environment_data` that takes a string `data` as input, extracts temperature, CO2 levels, and ice caps status using regular expressions, and returns them as separate lists of matches. The data is assumed to be in the format "Temperature: <number>", "CO2: <number>", and "IceCaps: <status>", where <number> is a floating-point number and <status> is any word.
"""

import re

def extract_environment_data(data):
    # Assuming data patterns as "Temperature: <number>", "CO2: <number>","IceCaps: <status>"
    temperature_pattern = r"Temperature: (\d+\.\d+)"
    co2_pattern = r"CO2: (\d+\.\d+)"
    ice_caps_pattern = r"IceCaps: (\w+)"

    temperature = re.findall(temperature_pattern, data)
    co2_levels = re.findall(co2_pattern, data)
    ice_caps_status = re.findall(ice_caps_pattern, data)
    
    return temperature, co2_levels, ice_caps_status