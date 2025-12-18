"""
QUESTION:
Write a function `extract_company_name(logo)` that takes a string `logo` representing an ASCII art logo and returns the company name as a string if it exists, or "Company name not found" otherwise. The company name is the text surrounded by '|' characters in the logo.
"""

import re

def extract_company_name(logo):
    matches = re.findall(r'\|(.+?)\|', logo)
    if matches:
        return matches[0].strip()
    else:
        return "Company name not found"