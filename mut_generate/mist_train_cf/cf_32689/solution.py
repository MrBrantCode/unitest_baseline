"""
QUESTION:
Create a function `validate_slug` that takes a string as input and returns "valid" if the input string is a valid "slug" and "invalid" otherwise. A valid "slug" consists only of lowercase letters (a-z), numbers (0-9), underscores (_), or hyphens (-), is not empty, and does not start or end with a hyphen or underscore.
"""

import re

def validate_slug(slug: str) -> str:
    if not slug:
        return "invalid"  
    if not re.match(r'^[a-z0-9_-]+$', slug):
        return "invalid"  
    if slug[0] in ('-', '_') or slug[-1] in ('-', '_'):
        return "invalid"  
    return "valid"