"""
QUESTION:
Create a function `generate_grocery_xml` that converts a given list of grocery items into an XML format. Each item should have properties like name, category, brand, quantity, and price. The function should ensure the validation of each item's properties before adding it to the list. The XML structure should have a root element called "grocery_list" and each item as a child element with attributes for the mentioned properties.
"""

import xml.etree.ElementTree as ET

def generate_grocery_xml(grocery_list):
    """
    Converts a given list of grocery items into an XML format.
    
    Args:
        grocery_list (list): A list of dictionaries containing grocery items with properties like name, category, brand, quantity, and price.
    
    Returns:
        root (Element): The root element of the XML structure.
    """
    # Create root element
    root = ET.Element("grocery_list")
    
    # Iterate through list of items and create child elements
    for item in grocery_list:
        # Create item element
        item_elem = ET.SubElement(root, "item")
        
        # Add attributes for name, category, brand, quantity, and price
        item_elem.set("name", item["name"])
        item_elem.set("category", item["category"])
        item_elem.set("brand", item["brand"])
        item_elem.set("quantity", str(item["quantity"]))
        item_elem.set("price", str(item["price"]))
    
    return root