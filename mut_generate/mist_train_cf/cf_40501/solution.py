"""
QUESTION:
Write a function called `parseCode` that takes a code snippet as input and returns a list of class and enum names found in the code snippet. The code snippet will only contain class and enum declarations, and the names will be alphanumeric strings. The function should extract the names from the declarations using the keywords 'class' and 'enum' followed by the name.
"""

import re

def parseCode(code):
    class_pattern = r'class\s+([A-Za-z0-9_]+)'
    enum_pattern = r'enum\s+([A-Za-z0-9_]+)'

    class_names = re.findall(class_pattern, code)
    enum_names = re.findall(enum_pattern, code)

    return class_names + enum_names