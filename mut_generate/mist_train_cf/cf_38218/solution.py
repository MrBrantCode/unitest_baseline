"""
QUESTION:
Implement the function `extract_field_names(model_definition: str) -> List[str]` that takes a string `model_definition` representing a Django model definition and returns a list of field names present in the model. The model definition string is a Python class definition with fields defined using Django's `models` module. Each field definition is on a separate line and may include various parameters and attributes. Assume the model definition string is well-formed and syntactically correct.
"""

from typing import List
import ast

def extract_field_names(model_definition: str) -> List[str]:
    field_names = []
    tree = ast.parse(model_definition)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
            field_names.append(node.targets[0].id)
    return field_names