"""
QUESTION:
Write a function `extract_license_info` that takes a string representing a license file as input and returns a dictionary containing the following extracted information:
- Copyright year
- Name of the copyright holder
- Email of the copyright holder
- License type and version
- URL to obtain a copy of the license

The input string may contain different variations of the license file format.
"""

import re

def extract_license_info(license_text):
    info = {}
    
    # Extract copyright year, holder, and email using regular expressions
    match = re.search(r'Copyright (\d{4}) (.+?) <(.+?)>', license_text)
    if match:
        info["copyright_year"] = match.group(1)
        info["copyright_holder"] = match.group(2)
        info["copyright_email"] = match.group(3)
    
    # Extract license type and version
    match = re.search(r'Licensed under the (.+?), Version (.+?) \(the "License"\)', license_text)
    if match:
        info["license_type"] = match.group(1)
        info["license_version"] = match.group(2)
    
    # Extract license URL
    match = re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', license_text)
    if match:
        info["license_url"] = match.group(0)
    
    return info