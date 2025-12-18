"""
QUESTION:
Implement the function `process_property_updates(person, property_updates)` to apply a list of property updates to a person object. 

The function should take two parameters: 
- `person`: A dictionary representing the person object where keys are property names and values are JSON objects.
- `property_updates`: A list of tuples containing the operation type, property key, and value. 

The function should apply the property updates to the person object and return the updated person object. The operation types are "set_once", "overwrite", and "unset", which set the property value if it is not already set, overwrite the property value with the given value, and remove the property from the person object respectively.
"""

def process_property_updates(person, property_updates):
    updated_person = person.copy()
    for operation, key, value in property_updates:
        if operation == 'set_once' and key not in updated_person:
            updated_person[key] = value
        elif operation == 'overwrite':
            updated_person[key] = value
        elif operation == 'unset' and key in updated_person:
            del updated_person[key]
    return updated_person