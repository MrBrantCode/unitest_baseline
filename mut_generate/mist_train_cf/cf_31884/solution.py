"""
QUESTION:
Create a function `analyze_license` that takes a multi-line string `license_text` as input and returns a dictionary with the extracted license details. The input `license_text` contains the type and version of the license in the format 'Licensed under the [type], [version] (the "License")' and may include URLs starting with 'https://'. The function should extract the license type, version, and URLs, and return them as a dictionary with keys 'type', 'version', and 'urls'.
"""

import re

def analyze_license(license_text: str) -> dict:
    result = {}
    
    match = re.search(r'Licensed under the (.+), (.+) \(the "License"\)', license_text)
    if match:
        result["type"] = match.group(1)
        result["version"] = match.group(2)
    
    urls = re.findall(r'https://\S+', license_text)
    result["urls"] = urls
    
    return result