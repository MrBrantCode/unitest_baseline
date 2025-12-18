"""
QUESTION:
Generate a function named `generate_url` that takes four string parameters (`protocol`, `subdomain`, `domain`, `path`) and one dictionary parameter (`query_parameters`). The function should concatenate these parameters to form a URL, encode the query parameters into a base64 format, and validate the resulting URL against a regular expression for URLs. The function should print whether the URL is valid or invalid and return the resulting URL.
"""

import re
import base64
from urllib.parse import urlencode

def generate_url(protocol, subdomain, domain, path, query_parameters):
    # Generate the raw URL from components
    raw_url = f"{protocol}://{subdomain}.{domain}/{path}?"

    # Encode the query parameters into base64 format
    encoded_params = base64.b64encode(urlencode(query_parameters).encode("utf-8"))
    raw_url += str(encoded_params, "utf-8").replace('=', '%3D')

    # Validate the URL
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.match(regex, raw_url) is None:
        print("Invalid URL")
    else:
        print("Valid URL")

    return raw_url