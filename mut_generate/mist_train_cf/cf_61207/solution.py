"""
QUESTION:
Create a function called `parse_url` that takes a URL string as an argument and returns a dictionary containing the subdomain, primary domain, country code Top-Level Domain (ccTLD), resource path, query parameters, and fragment identifier. The function should support various protocols like HTTP, HTTPS, and SFTP, and should handle Unicode characters in the URL, query parameters, and fragment identifiers. The function should also log and report any errors encountered while parsing and validating the URL, including unsupported protocols, missing URL components, invalid or inaccessible domains or subdomains, non-existent or inaccessible resource path endpoints, mismatching query-parameter keys and values, and malformed or irrelevant fragment identifiers. The function should be able to distinguish between POST and GET requests.
"""

from urllib.parse import urlparse, parse_qs

def parse_url(url):
    result = urlparse(url)
    return {
        "scheme": result.scheme,
        "subdomain": '.'.join(result.netloc.split('.')[:-2]),
        "primary_domain": '.'.join(result.netloc.split('.')[-2:]),
        "country_code_TLD": result.netloc.split('.')[-1],
        "resource_path": result.path,
        "query_parameters": parse_qs(result.query),
        "fragment_identifier": result.fragment
    }