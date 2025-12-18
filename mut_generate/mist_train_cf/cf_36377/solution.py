"""
QUESTION:
Implement a `s_get_full_url` function that constructs a full URL from a given relative URL and an optional base URL. The function should return the full URL as a string, handling cases where the base URL is not provided and correctly constructing the full URL based on the scheme, netloc, path, query, and fragment components. If the base URL is not provided, return the relative URL as the full URL.
"""

from urllib.parse import urlparse, urlunparse, ParseResult

def s_get_full_url(url, base=None):
    if not base:
        return url  # If base URL is not provided, return the relative URL as the full URL

    # Parse the base URL and relative URL
    base_parsed = urlparse(base)
    url_parsed = urlparse(url)

    # Construct the full URL based on the components
    full_url = ParseResult(
        scheme=url_parsed.scheme or base_parsed.scheme,
        netloc=url_parsed.netloc or base_parsed.netloc,
        path=url_parsed.path if url_parsed.path.startswith('/') else base_parsed.path + '/' + url_parsed.path if base_parsed.path and base_parsed.path.endswith('/') else base_parsed.path + url_parsed.path,
        params=url_parsed.params,
        query=url_parsed.query,
        fragment=url_parsed.fragment
    )

    return urlunparse(full_url)  # Return the full URL as a string