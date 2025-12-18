"""
QUESTION:
Write a function `parse_xml` that takes an XML file name as input and extracts the compound ID, compound name, molecular weight, and formula for each chemical compound entry in the XML file. The XML file is assumed to be well-formed and follows a specific format. After extracting the information, the function should calculate the average molecular weight of all compounds and identify the compound with the highest molecular weight. The function should be able to handle any number of compound entries in the XML file and return the average molecular weight and the ID and name of the compound with the highest molecular weight.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    """
    Parse the XML file and extract compound information.

    Args:
    xml_file (str): Name of the XML file.

    Returns:
    tuple: A tuple containing the average molecular weight and the ID and name of the compound with the highest molecular weight.
    """
    
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    compounds = []
    
    for compound in root.findall('compound'):
        compound_id = compound.find('id').text
        compound_name = compound.find('name').text
        molecular_weight = float(compound.find('molecular_weight').text)
        formula = compound.find('formula').text
        
        compounds.append({
            'id': compound_id,
            'name': compound_name,
            'molecular_weight': molecular_weight,
            'formula': formula
        })
    
    total_weight = sum(compound['molecular_weight'] for compound in compounds)
    average_weight = total_weight / len(compounds)
    
    max_weight_compound = max(compounds, key=lambda x: x['molecular_weight'])
    
    return average_weight, max_weight_compound['id'], max_weight_compound['name']