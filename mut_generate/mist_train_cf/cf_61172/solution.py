"""
QUESTION:
Write a function named `count_names` that takes an XML string as input, parses it, and returns a dictionary where keys are the text content of 'name' elements and values are their corresponding counts. The function should also print the text content of each 'name' element as it is encountered. The XML string can contain multiple 'name' elements with the same text content.
"""

import xml.etree.ElementTree as ET
from collections import defaultdict

def count_names(xml_string):
    """
    This function takes an XML string as input, parses it, and returns a dictionary 
    where keys are the text content of 'name' elements and values are their corresponding counts.
    
    Args:
        xml_string (str): The input XML string.
    
    Returns:
        dict: A dictionary with 'name' elements as keys and their counts as values.
    """
    # Parse the XML data
    root = ET.fromstring(xml_string)
    
    # Initialize a dictionary to count the occurrences of names
    name_counts = defaultdict(int)
    
    # Iterate over all 'name' elements in the document
    for name in root.iter('name'):
        # Extract the text content of the 'name' element
        name_text = name.text
        
        print(name_text)
        # Increment the count for this name
        name_counts[name_text] += 1
        
    return dict(name_counts)