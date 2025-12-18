"""
QUESTION:
Implement a function `text_to_filename(text, prefix=None, suffix=None)` that takes a string `text`, an optional string `prefix`, and an optional string `suffix`, and returns a valid filename. The function should remove any invalid characters (including `\/:*?"<>|`) from the text, replace spaces with underscores, and optionally prepend the `prefix` followed by an underscore and/or append the `suffix` preceded by a dot.
"""

import re

def text_to_filename(text, prefix=None, suffix=None):
    # Remove invalid characters and replace spaces with underscores
    filename = re.sub(r'[^\w\s-]', '', text).strip().replace(' ', '_')
    
    # Add prefix and suffix if provided
    if prefix:
        filename = f"{prefix}_{filename}"
    if suffix:
        filename = f"{filename}.{suffix}"
    
    return filename