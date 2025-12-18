"""
QUESTION:
Create a function named `extract_values` that takes a list of dictionaries as input. The function should exclude certain keys from being included in the extracted values, handle nested dictionaries by extracting their values, and perform a specific operation on each extracted value before returning the result. The function should return a list of extracted and modified values. The list of excluded keys and the specific operation to be performed on each value will be implemented within the function.
"""

def extract_values(data):
    extracted_values = []
    
    for dictionary in data:
        for key, value in dictionary.items():
            if key in ["key1", "key2"]:
                continue
            
            if isinstance(value, dict):
                extracted_values.extend(extract_values([value]))
                continue
            
            modified_value = value.upper()  
            extracted_values.append(modified_value)
    
    return extracted_values