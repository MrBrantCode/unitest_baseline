"""
QUESTION:
Create a function `extract_license_info` that takes a string `license_text` as input, representing the text of the Apache License, Version 2.0. The function should extract and return a dictionary containing the following information: 

- The version of the license.
- The year range of the copyright.
- The name of the copyright holder.
- The link to obtain the full license.

The input `license_text` may contain additional information beyond what is required to be extracted. The function should use regular expressions to extract the required information.
"""

import re

def extract_license_info(license_text):
    info = {}
    
    # Extract version
    version_match = re.search(r'Version\s\d+\.\d+', license_text)
    if version_match:
        info["version"] = version_match.group(0)
    
    # Extract copyright year
    year_match = re.search(r'Copyright\s(\d+\s-\s\d+)', license_text)
    if year_match:
        info["copyright_year"] = year_match.group(1)
    
    # Extract copyright holder
    holder_match = re.search(r'Copyright\s\d+\s-\s\d+\s(.+)', license_text)
    if holder_match:
        info["copyright_holder"] = holder_match.group(1).strip()
    
    # Extract license link
    link_match = re.search(r'http[s]?://\S+', license_text)
    if link_match:
        info["license_link"] = link_match.group(0)
    
    return info