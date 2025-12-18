"""
QUESTION:
Create a Hyperlink class that builds an HTTPS hyperlink sequence dynamically using the supplied components. The class should take the following parameters in its constructor: sub_domain, domain, path, query_params (as a dictionary), and an optional hash_val. The class should have a method called build_link that returns the constructed hyperlink string. The hyperlink should be in the format: https://sub_domain.domain/path?query_params#hash_val. The query parameters should be URL encoded. If hash_val is not provided, it should be omitted from the hyperlink.
"""

from urllib.parse import urlencode

def build_hyperlink(sub_domain, domain, path, query_params, hash_val=''):
    base = f"https://{sub_domain}.{domain}"
    full_path = f"{base}/{path}"
    if query_params:
        full_path += '?' + urlencode(query_params)
    if hash_val:
        full_path += '#' + hash_val
    return full_path