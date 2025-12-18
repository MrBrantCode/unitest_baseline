"""
QUESTION:
Create a function `count_imported_resources(code_snippet: str) -> dict` that takes a Python code snippet as a string and returns a dictionary containing the count of each resource imported from the `terrascript` module. The code snippet may contain multiple import statements from the `terrascript` module. The function should return a dictionary where the keys are the imported resource names and the values are the counts of each resource imported. The length of the code snippet is between 1 and 1000 characters.
"""

import re

def count_imported_resources(code_snippet: str) -> dict:
    imports = re.findall(r'from\s+terrascript\.resource\..+?\.cosmic\s+import\s+(\w+)', code_snippet)
    resource_counts = {}
    for resource in imports:
        resource_counts[resource] = resource_counts.get(resource, 0) + 1
    return resource_counts