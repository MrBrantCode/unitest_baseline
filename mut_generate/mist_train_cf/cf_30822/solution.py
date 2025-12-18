"""
QUESTION:
Create a function `extract_class_names` that takes a string of HTML code as input and returns a list of unique class names in the order of their first occurrence. Class names are case-sensitive, specified within the `class` attribute of HTML elements, and separated by spaces.
"""

from typing import List
import re

def extract_class_names(html_code: str) -> List[str]:
    class_names = re.findall(r'class="([^"]+)"', html_code)  # Extracts the content within the class attribute
    unique_class_names = set()
    ordered_class_names = []
    for names in class_names:
        for name in names.split():  # Splits the class names
            if name not in unique_class_names:  # Check if the class name has not been added yet
                unique_class_names.add(name)
                ordered_class_names.append(name)  # Add the class name to the ordered list
    return ordered_class_names