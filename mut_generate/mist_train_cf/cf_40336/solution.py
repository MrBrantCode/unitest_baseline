"""
QUESTION:
Write a function `transform_relative_imports` that takes a package name, a string containing import statements, and a list of tuples representing the original import statements and their expected transformed results. It should transform the import statements in the string based on the provided package and compare the results with the expected transformed import statements. The function should return a list of transformed import statements. The package name should be used to replace relative imports in the string, for example, transforming "from . import util" to "from autofit.tools import util" if the package is "autofit".
"""

from typing import List, Tuple

def transform_relative_imports(package: str, string: str, transformations: List[Tuple[str, str]]) -> List[str]:
    transformed_imports = []
    for original, expected in transformations:
        if original in string:
            transformed_import = string.replace(original, expected)
            transformed_imports.append(transformed_import)
    return transformed_imports