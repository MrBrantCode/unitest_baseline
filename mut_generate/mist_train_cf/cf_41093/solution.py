"""
QUESTION:
Create a function `validate_metadata(package_name: str) -> bool` that takes a package name as input and returns `True` if the package has the metadata attributes "author", "contact", "license", and "version", and they are all of type string. The function should return `False` otherwise. Assume that the package is installed and can be imported using the provided package name.
"""

import importlib

def validate_metadata(package_name: str) -> bool:
    try:
        package = importlib.import_module(package_name)
        metadata_attributes = ["author", "contact", "license", "version"]
        for attr in metadata_attributes:
            real_attr = f"__{attr}__"
            if not hasattr(package, real_attr) or not isinstance(getattr(package, real_attr), str):
                return False
        return True
    except ImportError:
        return False