"""
QUESTION:
Create a function named `parse_street_info` that takes a geospatial string as input and returns a tuple containing the street number and street name. The function should use regular expressions to extract the street number and name from the string, capturing the street number as one group and the street name along with common street types (St, Rd, Ave, Blvd, Dr, Ln) as another group.
"""

import re

def parse_street_info(geospatial_string):
    """
    This function takes a geospatial string as input and returns a tuple containing 
    the street number and street name. It uses regular expressions to extract the 
    street number and name from the string.

    Args:
        geospatial_string (str): The input geospatial string.

    Returns:
        tuple: A tuple containing the street number and street name.
    """

    # setting up a regular expression pattern to capture 
    # first group - the street number
    # second group - the street name and street type
    reg_pattern = r"(\d*)\s*([a-zA-Z\s]*)(St|Rd|Ave|Blvd|Dr|Ln)"

    match = re.search(reg_pattern, geospatial_string)

    if match:
        return (match.group(1), match.group(2))
    else:
        return None