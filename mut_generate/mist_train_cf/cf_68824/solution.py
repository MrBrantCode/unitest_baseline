"""
QUESTION:
Implement a function `add_cors_headers` that takes a dictionary `headers` and a list `allowed_domains` as parameters. The function should add the necessary CORS headers to the `headers` dictionary to allow cross-origin resource sharing from the domains specified in `allowed_domains`. The function should add the 'Access-Control-Allow-Origin' header with the specified domains and set the 'Access-Control-Allow-Methods' header to 'GET, POST, PUT, DELETE, OPTIONS'.
"""

def add_cors_headers(headers, allowed_domains):
    """
    Adds the necessary CORS headers to the headers dictionary to allow cross-origin resource sharing from the domains specified in allowed_domains.
    
    Args:
        headers (dict): A dictionary of HTTP headers.
        allowed_domains (list): A list of domains allowed for cross-origin resource sharing.
    
    Returns:
        dict: The updated headers dictionary with CORS headers.
    """
    headers['Access-Control-Allow-Origin'] = ', '.join(allowed_domains)
    headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    return headers