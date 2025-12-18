"""
QUESTION:
Create a function `validate_url(url)` that checks if a given URL is correctly formatted, uses HTTPS encryption, and has a top-level domain from a predefined list of approved TLDs. The function should be able to handle URLs with or without 'www' prefixes, extract and print the domain name, and return a corresponding message indicating the validation result. The approved TLDs are .com, .edu, and .org. The function should return a string describing the validation result.
"""

import re

def validate_url(url):
    # Define regex string
    pattern = r'https://(www\.)?([\w\-]+)(\.\w+)$'

    # Define approved tld
    approved_tld = ['.com', '.edu', '.org']

    # Match URL with pattern
    re_match = re.match(pattern, url)

    if re_match is None:
        return "Invalid URL format. Make sure it follows the structure 'https://www.example.com'."
    
    domain = re_match.group(2)
    tld = re_match.group(3)
    print("Domain name: ", domain)

    if tld in approved_tld:
        return "URL is correctly formatted, uses HTTPS encryption and top-level domain is approved."
    else:
        return "URL is correctly formatted and uses HTTPS encryption, but top-level domain is not approved."