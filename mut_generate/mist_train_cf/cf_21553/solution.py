"""
QUESTION:
Write a function called `parse_url` that takes a string as input and returns a dictionary containing the URL's protocol, domain, path, query parameters, and hash fragment. The input URL will always be well-formed and include a protocol, a domain, and may include a path, query parameters, and a hash fragment. The function should not use any built-in URL parsing or query string parsing libraries or functions.
"""

def parse_url(url):
    # Find the protocol
    protocol_end = url.find("://")
    protocol = url[:protocol_end]
    remaining_url = url[protocol_end+3:]

    # Find the domain
    domain_end = remaining_url.find("/")
    domain = remaining_url[:domain_end]
    remaining_url = remaining_url[domain_end:]

    # Find the path
    path_end = remaining_url.find("?")
    if path_end == -1:
        path_end = remaining_url.find("#")
    if path_end == -1:
        path_end = len(remaining_url)
    path = remaining_url[:path_end]
    remaining_url = remaining_url[path_end:]

    # Find the query parameters
    query_params = {}
    if remaining_url.startswith("?"):
        query_end = remaining_url.find("#")
        if query_end == -1:
            query_end = len(remaining_url)
        query_string = remaining_url[1:query_end]
        query_pairs = query_string.split("&")
        for pair in query_pairs:
            key, value = pair.split("=")
            query_params[key] = value
        remaining_url = remaining_url[query_end:]

    # Find the hash fragment
    hash_fragment = ""
    if remaining_url.startswith("#"):
        hash_fragment = remaining_url[1:]

    # Create the result dictionary
    result = {
        "protocol": protocol,
        "domain": domain,
        "path": path,
        "query_params": query_params,
        "hash": hash_fragment
    }

    return result