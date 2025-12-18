"""
QUESTION:
Write a function `panos_url_formatting` that takes in a JSON object `iocs_json` containing indicators of compromise (IOCs) in the form of key-value pairs, a boolean flag `drop_invalids` to indicate whether invalid indicators should be dropped or not, and a boolean flag `strip_port` to indicate whether port numbers should be stripped from the URLs or not. The function should return a tuple containing a dictionary with the formatted URLs after processing the indicators and the number of indicators after processing.
"""

import re

def panos_url_formatting(iocs_json, drop_invalids, strip_port):
    formatted_urls = {}
    total_indicators = 0

    for indicator_type, indicators in iocs_json.items():
        formatted_indicators = []
        for indicator in indicators:
            if ":" in indicator and strip_port:
                indicator = re.sub(r':\d+', '', indicator)  # Remove port number
            if drop_invalids and ":" in indicator:
                continue  # Skip invalid indicator with port number
            formatted_indicators.append(indicator)
        formatted_urls[indicator_type] = formatted_indicators
        total_indicators += len(formatted_indicators)

    return formatted_urls, total_indicators