"""
QUESTION:
Implement a function `extract_class_info(code: str) -> dict` that takes a string `code` as input and returns a dictionary. The dictionary should contain class names as keys and tuples of their associated forms and icons as values. The function should process the given `code` string, extracting the class names, associated forms, and icons. If an icon is not specified for a class, its value should be `None` in the dictionary. The class names are in the format `ClassName`, form names are in the format `addClassNameForm`, and icon paths are relative and start with `'www/'`.
"""

import re

def extract_class_info(code: str) -> dict:
    class_info = {}
    class_pattern = r'context\.registerClass\((\w+),\s+constructors=\((\w+),\s*(\w+)?\),\s*icon=\'(www\/\w+\.gif)?\'\)'
    matches = re.findall(class_pattern, code)

    for match in matches:
        class_name = match[0]
        form_name = match[1]
        icon = match[3] if match[3] else None
        class_info[class_name] = (form_name, icon)

    return class_info