"""
QUESTION:
Write a function `parseFoodProductXML` that takes in XML data as a string, a nutrient code, and an allergen code. The function should return the nutrient value for the given code rounded to two decimal places and a boolean indicating whether the specified allergen is contained in the product.

The XML data contains information about food products with the following structure: 
- The `Allergens` section contains one or more `Allergen` elements with a `contained` attribute and the allergen code as text.
- The `NutrientValues` section contains one or more `NutrientValue` elements with a `code` attribute and the nutrient value as text.

The function should find the nutrient value for the given code in the `NutrientValues` section and check if the specified allergen is contained in the product by searching for the allergen code in the `Allergens` section and checking its `contained` attribute.
"""

import xml.etree.ElementTree as ET

def parseFoodProductXML(xml_data: str, nutrient_code: str, allergen_code: str) -> (float, bool):
    root = ET.fromstring(xml_data)
    
    # Extract nutrient value for the given code
    nutrient_value = None
    nutrient_values = root.find('NutrientValues')
    for nutrient in nutrient_values.findall('NutrientValue'):
        if nutrient.attrib['code'] == nutrient_code:
            nutrient_value = round(float(nutrient.text), 2)
            break
    
    # Check if the specified allergen is contained in the product
    allergen_contained = False
    allergens = root.find('Allergens')
    for allergen in allergens.findall('Allergen'):
        if allergen.text == allergen_code:
            allergen_contained = allergen.attrib['contained'] == 'YES'
            break
    
    return nutrient_value, allergen_contained