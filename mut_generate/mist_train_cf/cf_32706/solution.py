"""
QUESTION:
Implement the function `validate_trial_data(data, schema)` that takes two parameters: 
- `data`: a dictionary representing a trial record with field names as keys and corresponding values.
- `schema`: a dictionary representing the schema with field names as keys and corresponding expected data types ('str', 'bool', 'list[str]') as values.

The function should return `True` if all the fields in the `data` match the expected data types specified in the `schema`, and `False` otherwise.
"""

def validate_trial_data(data, schema):
    for field, expected_type in schema.items():
        if field not in data:
            return False  
        if expected_type == 'str' and not isinstance(data[field], str):
            return False  
        elif expected_type == 'bool' and not isinstance(data[field], bool):
            return False  
        elif expected_type == 'list[str]' and not isinstance(data[field], list):
            return False  
        elif expected_type == 'list[str]' and not all(isinstance(item, str) for item in data[field]):
            return False  
    return True  