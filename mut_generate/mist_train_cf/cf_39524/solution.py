"""
QUESTION:
Write a function `parseLicense` that takes a string as input and returns a dictionary. The input string represents a software license and is expected to be in the format:
```
// License: <license_type>
// Permissions: <comma_separated_permissions>
// Limitations: <comma_separated_limitations>
```
The function should extract the license type, permissions, and limitations and return them in a dictionary with the keys "license_type", "permissions", and "limitations". If the input string does not match the expected format, the function should return `None`.
"""

def parseLicense(license_text):
    lines = license_text.split('\n')
    if len(lines) != 3 or not all(line.startswith('// ') for line in lines):
        return None
    license_type = lines[0][11:].strip()
    permissions = [p.strip() for p in lines[1][14:].split(',')]
    limitations = [l.strip() for l in lines[2][14:].split(',')]
    return {
        "license_type": license_type,
        "permissions": permissions,
        "limitations": limitations
    }