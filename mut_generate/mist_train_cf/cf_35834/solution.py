"""
QUESTION:
Create a function named `get_imported_models` that takes the name of a subpackage as input and returns a list of model names imported from that subpackage. The function should dynamically import the models from the specified subpackage and identify the model names by checking if the attributes of the imported module are classes. If the subpackage or models are not found, the function should return an empty list. The function should be designed to work with a project structure where the subpackage is a subdirectory of a package, and the models are defined in a `models.py` file within the subpackage.
"""

from typing import List
import importlib

def get_imported_models(subpackage_name: str) -> List[str]:
    imported_models = []
    try:
        subpackage = importlib.import_module(f'.{subpackage_name}.models', package='package')
        for name in dir(subpackage.models):
            obj = getattr(subpackage.models, name)
            if isinstance(obj, type):
                imported_models.append(name)
    except ModuleNotFoundError:
        pass
    return imported_models