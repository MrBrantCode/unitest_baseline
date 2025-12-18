"""
QUESTION:
Create a function called `extract_package_name` that takes a code snippet as input and returns the package name following the last occurrence of the word "import" in the code snippet. If no import statements are found, the function should return "No package imported". The function should be able to extract the package name even if the import statement is commented out.
"""

import re

def extract_package_name(code_snippet):
    import_statement = re.findall(r'import\s+(\w+)', code_snippet)
    if import_statement:
        return import_statement[-1]
    else:
        return "No package imported"