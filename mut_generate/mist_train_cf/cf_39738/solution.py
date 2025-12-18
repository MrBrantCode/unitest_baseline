"""
QUESTION:
Create a Python function `extract_migration_fields` that takes a list of strings representing Django migration files and a model name as input, and returns a list of tuples containing the model name, field name, and field type for each field being added to the specified model. The function should return an empty list if the model name does not exist in any of the migration files.
"""

from typing import List, Tuple
import re

def extract_migration_fields(migration_files: List[str], model_name: str) -> List[Tuple[str, str, str]]:
    fields = []
    for migration_file in migration_files:
        model_pattern = r"model_name='{}'".format(model_name)
        matches = re.findall(model_pattern, migration_file)
        if matches:
            field_pattern = r"migrations\.AddField\(\s*model_name='{}',\s*name='(\w+)',\s*field=models\.(\w+)\(".format(model_name)
            field_matches = re.findall(field_pattern, migration_file)
            for match in field_matches:
                fields.append((model_name, match[0], match[1]))
    return fields