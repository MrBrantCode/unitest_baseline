"""
QUESTION:
Implement a function `findNameMaterial(material_name, existing_materials, counter)` that takes a string representing the material name, a list of existing materials, and a counter as input. The function should remove unorthodox characters (non-alphanumeric and non-space characters) from the material name and create a unique name by appending the counter if the cleaned name already exists in the list of materials. If the material name does not exist in the list, it should remain unchanged. The function should return the modified material name.
"""

def findNameMaterial(material_name, existing_materials, counter):
    clean_name = ''.join(e for e in material_name if e.isalnum() or e.isspace())
    unique_name = clean_name
    while unique_name in existing_materials:
        unique_name = f"{clean_name}_{counter}"
        counter += 1
    return unique_name