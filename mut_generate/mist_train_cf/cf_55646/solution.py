"""
QUESTION:
Create a function named `extract_data` in Python that uses regular expressions to extract the following data points from a given environmental source: global temperature records, production levels of carbon dioxide, methane, and nitrous oxide, the degradation status of polar ice caps, the deforestation rate, and the extinction rate of various species. The function should be able to handle different formatting and structuring styles of the input source. 

Additionally, the function should be able to detect and manage anomalies in the extracted data. For the purpose of this task, consider any negative value as an anomaly. The function should return a structured dictionary containing the extracted data with anomalies marked accordingly.
"""

import re

def extract_data(source):
    '''This function tries to extract meaningful data from source using regex'''

    # initialize dictionary to store extracted data
    data = {
        'temperature': None,
        'co2': None,
        'methane': None,
        'nitrous_oxide': None,
        'ice_caps': None,
        'deforestation_rate': None,
        'extinction_rate': None,
    }

    # regex patterns to match
    patterns = {
        'temperature': r'global temperature records:\s*([+-]?\d+(?:\.\d+)?)',
        'co2': r'carbon dioxide production levels:\s*([+-]?\d+(?:\.\d+)?)',
        'methane': r'methane production levels:\s*([+-]?\d+(?:\.\d+)?)',
        'nitrous_oxide': r'nitrous oxide production levels:\s*([+-]?\d+(?:\.\d+)?)',
        'ice_caps': r'polar ice caps degradation status:\s*([\w\s]+)',
        'deforestation_rate': r'deforestation rate:\s*([+-]?\d+(?:\.\d+)?)',
        'extinction_rate': r'extinction rate:\s*([+-]?\d+(?:\.\d+)?)',
    }

    # iterate over all required data points
    for key, pattern in patterns.items():
        match = re.search(pattern, source, re.IGNORECASE)
        if match:
            value = match.group(1)
            # handle anomalies based on domain knowledge - usually requires expert input
            # for simplicity let's consider values below 0 as anomalies
            if key in ['temperature', 'co2', 'methane', 'nitrous_oxide', 'deforestation_rate', 'extinction_rate']:
                if float(value) < 0:
                    data[key] = f'Anomaly detected: {value}'
                else:
                    data[key] = value
            else:
                data[key] = value

    return data