"""
QUESTION:
Create a function named `parse_data` that extracts environmental data from unstructured text, handling inconsistencies and variations in unit measurements. The function should take a list of strings as input, where each string represents a line of data. It should return a list of dictionaries, where each dictionary contains the extracted variable name, unit, and value.

The function should be able to handle varying units of measurement (e.g., degrees Celsius/Fahrenheit for temperature, metric/imperial units for ice sheet areas) and linguistic variations in the text data. It should also be efficient and readable, allowing for easy adjustments to the regex patterns as the data format changes over time.
"""

import re

def parse_data(data):
    variable_patterns = {
        'temperature': r'\btemperature\b',
        'co2_emissions': r'\bcarbon\s*dioxide\s*emissions\b',
        'polar_ice': r'\bpolar\s*ice\s*sheets\b',
        # add more as needed
    }

    unit_patterns = {
        'celsius': r'\b(degrees*\s*celsius|c)\b',
        'fahrenheit': r'\b(degrees*\s*fahrenheit|f)\b',
        'metric': r'\b(metric|km\^2)\b',
        'imperial': r'\b(imperial|mi\^2)\b',
        # add more as needed
    }

    result = []
    for line in data:
        line_result = {}
        for variable, pattern in variable_patterns.items():
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                line_result['variable'] = variable
        for unit, pattern in unit_patterns.items():
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                line_result['unit'] = unit
        if 'variable' in line_result:
            line = re.sub(r'[^0-9.]', '', line)   # remove non-numeric chars
            line_result['value'] = float(line)
            result.append(line_result)
    return result