"""
QUESTION:
Create a function called `generate_parable` that takes an XML string as input, parses the XML data, and extracts the characters and their roles. The XML string should contain a `parable` element with `characters` and `story` elements. The `characters` element should contain `character` elements with `name` and `role` attributes, and the `story` element should contain `scene` elements with text content. The function should return a string that includes the list of characters and their roles, followed by the story. The input XML string may contain a scenario where one of the characters has a personal issue that is impacting their work.
"""

import xml.etree.ElementTree as ET

def generate_parable(xml_data):
    """
    This function generates a parable from an XML string.
    
    Parameters:
    xml_data (str): The XML string containing the parable data.
    
    Returns:
    str: A string representing the parable, including characters and their roles, followed by the story.
    """
    
    # Parse the XML data
    root = ET.fromstring(xml_data)
    
    # Extract the characters and their roles
    characters = {}
    for character in root.find('characters'):
        name = character.get('name')
        role = character.get('role')
        characters[name] = role
    
    # Generate the parable string
    parable = "In this parable, we have the following characters:\n"
    for name, role in characters.items():
        parable += f"{name} - {role}\n"
    parable += "\nHere is the story:\n"
    for scene in root.find('story'):
        parable += scene.text + "\n"
    
    return parable