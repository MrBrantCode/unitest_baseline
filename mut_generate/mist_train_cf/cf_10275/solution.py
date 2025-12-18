"""
QUESTION:
Write a function `extract_values` that takes a list of dictionaries as input, extracts all the values excluding certain keys, handles nested dictionaries, and performs an additional operation on each extracted value. The function should return a list of the modified extracted values. The excluded keys are "key1" and "key2", and the additional operation is converting the value to uppercase. The function should handle nested dictionaries of arbitrary depth.
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