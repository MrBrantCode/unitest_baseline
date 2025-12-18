"""
QUESTION:
Create a function `add_query_params` that takes in a URL and a dictionary of query parameters to add, and returns the modified URL with the new query parameters added. The function should handle cases where the URL already contains query parameters, ensuring that the new parameters are appended appropriately. The function should also handle edge cases such as empty input URL, empty new parameters dictionary, and URL with no existing query parameters.
"""

from urllib.parse import urlparse, urlencode, parse_qs, urlunparse

def add_query_params(url: str, new_params: dict) -> str:
    parsed_url = urlparse(url)
    existing_params = parse_qs(parsed_url.query)
    existing_params.update(new_params)
    updated_query = urlencode(existing_params, doseq=True)
    updated_url = parsed_url._replace(query=updated_query).geturl()
    return updated_url