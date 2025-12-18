"""
QUESTION:
Create a function `extract_model_names(migration_files)` that takes a list of migration file strings as input and returns a list of model names extracted from the `migrations.CreateModel` function calls. The model names are enclosed in single quotes after the `name=` parameter within the `migrations.CreateModel` function call. The model names may contain alphanumeric characters, underscores, and other valid Python identifier characters. The function should be efficient and able to handle multiple migration files.
"""

from typing import List
import re

def extract_model_names(migration_files: List[str]) -> List[str]:
    model_names = []
    for migration_file in migration_files:
        match = re.search(r"migrations\.CreateModel\(name='(\w+)'", migration_file)
        if match:
            model_names.append(match.group(1))
    return model_names