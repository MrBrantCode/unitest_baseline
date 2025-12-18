"""
QUESTION:
Write a function `transform_json` that takes a JSON string representing a person's information as input and returns a modified JSON string. The function should perform the following transformations: 
- replace the "name" field with its uppercase version, 
- convert the "age" field value to a string and append " years" to it, 
- change the date format of the "birthday" field from "YYYY-MM-DD" to "DD/MM/YYYY", and 
- multiply the "decimal_value" field within the "nested_field" by 2 and round it to the nearest integer.
"""

import json

def transform_json(person_json: str) -> str:
    person_data = json.loads(person_json)
    
    # Transformation 1: Uppercase the name
    person_data["name"] = person_data["name"].upper()
    
    # Transformation 2: Convert age to string and append " years"
    person_data["age"] = str(person_data["age"]) + " years"
    
    # Transformation 3: Change date format of birthday
    birthday_parts = person_data["birthday"].split("-")
    person_data["birthday"] = f"{birthday_parts[2]}/{birthday_parts[1]}/{birthday_parts[0]}"
    
    # Transformation 4: Multiply and round the decimal value
    person_data["nested_field"]["decimal_value"] = round(float(person_data["nested_field"]["decimal_value"]) * 2)
    
    return json.dumps(person_data)