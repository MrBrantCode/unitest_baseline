"""
QUESTION:
Define a function called `validate_entity` that takes a dictionary representing an entity with "name", "age", and "sex" attributes. The function should validate the entity's attributes according to the following rules: 
- The "sex" attribute must be one of "male", "female", or "non-binary" (case-insensitive).
- The "age" attribute must be numeric and within the range of 0 to 120.
The function should return a boolean indicating whether the entity's attributes are valid, or print an error message if the validation fails.
"""

def validate_entity(entity):
    acceptable_sex = ["male", "female", "non-binary"]
    
    if entity["sex"].lower() not in acceptable_sex:
        print(f"Invalid gender type for {entity['name']}. Must be either 'male', 'female' or 'non-binary'.")
        return False
    
    if not isinstance(entity["age"], int):
        if str(entity["age"]).isdigit():
            entity["age"] = int(entity["age"])
        else:
            print(f"Invalid age for {entity['name']}. Age must be a numeric value.")
            return False
        
    if entity["age"] < 0 or entity["age"] > 120:
        print(f"Invalid age for {entity['name']}. Age must be within the range 0 and 120.")
        return False
    
    return True