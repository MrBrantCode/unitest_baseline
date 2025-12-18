"""
QUESTION:
Write a function `extractClassNames` that takes a string `htmlSnippet` representing a well-formed HTML snippet as input and returns a list of unique class names found within the snippet. The class names are defined within the `class` attribute of HTML elements and are separated by spaces.
"""

import re

def extractClassNames(htmlSnippet):
    class_regex = r'class="([^"]+)"'
    class_names = re.findall(class_regex, htmlSnippet)
    
    unique_class_names = set()
    for classes in class_names:
        unique_class_names.update(classes.split())
    
    return list(unique_class_names)