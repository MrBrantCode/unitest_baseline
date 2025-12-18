"""
QUESTION:
Modify the `kebabize` function so that it converts a camel case string into a kebab case.

Notes:
  - the returned string should only contain lowercase letters
"""

def convert_camel_to_kebab(s: str) -> str:
    return ''.join((c if c.islower() else '-' + c.lower() for c in s if c.isalpha())).strip('-')