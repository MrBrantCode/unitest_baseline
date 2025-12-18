"""
QUESTION:
Implement the function `validate_data(data, rules)` where `data` is a dictionary representing the input data to be validated, and `rules` is a list of dictionaries representing the validation rules. Each rule dictionary contains the keys 'name', 'description', 'in', and 'type'. The function should return True if the input data adheres to all the specified rules, and False otherwise. The validation checks if each field specified in the rules exists in the input data at the specified location ('in' key) and matches the expected type ('type' key).
"""

def validate_data(data, rules):
    for rule in rules:
        field_name = rule['name']
        field_description = rule['description']
        field_location = rule['in']
        expected_type = rule['type']

        if field_name in data and field_location in data:
            if not isinstance(data[field_name], expected_type):
                return False
        else:
            return False

    return True