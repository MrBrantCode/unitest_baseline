"""
QUESTION:
Create a `FieldProcessor` class with an initializer that takes a dictionary `data` and an object `FieldClass`. The class should have two methods: `validate_data` and `process_data`. The `validate_data` method should return `True` if all fields in the data dictionary are valid according to the `FieldClass` definitions, and `False` otherwise. The `process_data` method should return a new dictionary containing the processed data according to the rules defined in the `FieldClass`. Assume the `FieldClass` object has methods `validate` and `process` to validate and process a specific field type.
"""

def create_field_processor(data: dict, FieldClass: object):
    for field, value in data.items():
        if not FieldClass.validate(field, value):
            return False
    processed_data = {}
    for field, value in data.items():
        processed_data[field] = FieldClass.process(field, value)
    return processed_data