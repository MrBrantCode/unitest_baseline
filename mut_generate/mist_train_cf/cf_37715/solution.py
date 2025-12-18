"""
QUESTION:
Implement a function `extract_weather_info(raw_text: str) -> dict` that takes a raw text input as a parameter. The function should extract weather information based on the regular expression pattern `r"\b(?P<type>(?:%(types)s))(?P<height>\d{3})?(?P<cb_tcu>CB|TCU)?\b"` where `types` are predefined weather condition types. 

The function should return a dictionary containing the extracted weather information with the keys "type", "height", and "cb_tcu", representing the type of weather condition, the height of the weather condition, and the presence of CB or TCU clouds respectively. If any information is not available, it should be represented as `None`. If no match is found, the function should return an empty dictionary.
"""

import re
from typing import Dict

def extract_weather_info(raw_text: str) -> Dict[str, str]:
    """Extracts weather information from the given raw text.

    Args:
    raw_text (str): The raw text containing weather information.

    Returns:
    Dict[str, str]: A dictionary containing the extracted weather information.
    """
    types = ["RA", "SN", "BR", "FG", "HZ"]  # Predefined weather condition types
    pattern = r"\b(?P<type>(?:%(types)s))(?P<height>\d{3})?(?P<cb_tcu>CB|TCU)?\b" % {"types": "|".join(types)}
    match = re.search(pattern, raw_text)
    if match:
        weather_info = {
            "type": match.group("type"),
            "height": match.group("height") if match.group("height") else None,
            "cb_tcu": match.group("cb_tcu") if match.group("cb_tcu") else None
        }
        return weather_info
    else:
        return {}  # Return an empty dictionary if no match is found