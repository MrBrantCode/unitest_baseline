"""
QUESTION:
Create a function `parse_individuals` that takes a string of XML data representing a list of individuals as input, extracts the individual profiles, and returns a list of dictionaries where each dictionary contains the profile of an individual. The XML data should be in the following format:
```
<individuals>
    <individual>
        <name>...</name>
        <age>...</age>
        <country>...</country>
        <profession>...</profession>
        <married>...</married>
    </individual>
    ...
</individuals>
```
Each dictionary in the output list should have the keys 'name', 'age', 'country', 'profession', and 'married'.
"""

import xml.etree.ElementTree as ET

def parse_individuals(xml_data):
    """
    This function takes a string of XML data representing a list of individuals, 
    extracts the individual profiles, and returns a list of dictionaries where 
    each dictionary contains the profile of an individual.
    
    Args:
    xml_data (str): A string of XML data.
    
    Returns:
    list: A list of dictionaries where each dictionary contains the profile of an individual.
    """
    
    # Parse the XML data into an ElementTree object
    root = ET.fromstring(xml_data)
    
    # Initialize an empty list to store the individual profiles
    profiles = []
    
    # Iterate over each individual in the XML data
    for individual in root:
        # Initialize an empty dictionary to store the profile of the current individual
        profile = {}
        
        # Iterate over each characteristic of the current individual
        for characteristic in individual:
            # Add the characteristic to the profile dictionary
            profile[characteristic.tag] = characteristic.text
        
        # Add the profile of the current individual to the list of profiles
        profiles.append(profile)
    
    # Return the list of profiles
    return profiles