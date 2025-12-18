"""
QUESTION:
Implement the `extract_model_info(model_definition: str) -> dict` function to process a Django model definition string and extract information about the fields and their relationships. The model definition string will be in the format:
 
    migrations.CreateModel(
        name='YourModelName',
        fields=[
            ('field1', models.FieldType()),
            ('field2', models.RelatedFieldType(to='related_model')),
            ...
        ],
    ),
 
The function should return a dictionary containing the model name, field names and their types, and relationship fields and their related model names.
"""

import re

def extract_model_info(model_definition: str) -> dict:
    model_info = {}
    
    # Extract model name
    model_name_match = re.search(r"name='(\w+)'", model_definition)
    if model_name_match:
        model_info['model_name'] = model_name_match.group(1)
    
    # Extract fields and their types
    fields_info = {}
    related_models = {}
    fields_matches = re.findall(r"\('(\w+)', models\.(\w+)\((.*?)\)", model_definition)
    for field_name, field_type, field_params in fields_matches:
        fields_info[field_name] = field_type
        if field_type.startswith('ForeignKey'):
            related_model_match = re.search(r"to='(\w+)'", field_params)
            if related_model_match:
                related_models[field_name] = related_model_match.group(1)
    
    model_info['fields'] = fields_info
    model_info['related_models'] = related_models
    
    return model_info