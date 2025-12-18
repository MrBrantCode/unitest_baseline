"""
QUESTION:
Write a function `check_duplicate_lightning_message_channel` to troubleshoot "duplicate value found" error when creating a Lightning Message Channel in Salesforce. The function should take an XML file content as input and return a list of potential duplicate values that may cause the error. 

The function should assume that the 'masterLabel' and 'fieldName' values in the XML file are unique identifiers and may cause the error if they already exist in Salesforce. 

The function should also check for other unique elements in the XML file that may cause the error.
"""

def check_duplicate_lightning_message_channel(xml_content):
    """
    This function takes an XML file content as input, parses it and returns a list of potential duplicate values 
    that may cause the "duplicate value found" error when creating a Lightning Message Channel in Salesforce.

    Args:
        xml_content (str): The content of the XML file.

    Returns:
        list: A list of potential duplicate values.
    """

    import xml.etree.ElementTree as ET

    # Parse the XML content
    root = ET.fromstring(xml_content)

    # Initialize a set to store unique values
    unique_values = set()

    # Initialize a list to store potential duplicate values
    duplicate_values = []

    # Iterate over all elements in the XML
    for elem in root.iter():
        # Check if the element has a 'masterLabel' or 'fieldName' attribute
        if 'masterLabel' in elem.attrib or 'fieldName' in elem.attrib:
            # Get the value of the 'masterLabel' or 'fieldName' attribute
            value = elem.attrib.get('masterLabel') or elem.attrib.get('fieldName')

            # Check if the value is already in the set of unique values
            if value in unique_values:
                # If the value is already in the set, add it to the list of duplicate values
                duplicate_values.append(value)
            else:
                # If the value is not in the set, add it to the set
                unique_values.add(value)

    # Return the list of potential duplicate values
    return duplicate_values