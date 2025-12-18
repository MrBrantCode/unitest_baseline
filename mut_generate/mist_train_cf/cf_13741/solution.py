"""
QUESTION:
Write a function `parse_url` that takes a well-formed URL string as input and returns a dictionary containing its component parts. The dictionary should include the protocol, domain, path, and any query parameters. The input URL will always include a protocol and may include subdomains, multiple path segments separated by slashes, and multiple query parameters separated by ampersands. The parsing logic must be implemented manually without using any built-in URL parsing or query string parsing libraries or functions.
"""

def parse_url(url):
    result = {}
    
    # Parse protocol
    protocol_end = url.find("://")
    result["protocol"] = url[:protocol_end]
    
    # Parse domain
    domain_start = protocol_end + 3
    domain_end = url.find("/", domain_start)
    result["domain"] = url[domain_start:domain_end]
    
    # Parse path
    path_start = domain_end
    query_start = url.find("?", path_start)
    if query_start == -1:
        path_end = len(url)
    else:
        path_end = query_start
    result["path"] = url[path_start:path_end]
    
    # Parse query parameters
    if query_start != -1:
        query_start += 1
        query_string = url[query_start:]
        query_params = {}
        query_pairs = query_string.split("&")
        for pair in query_pairs:
            key_value = pair.split("=")
            query_params[key_value[0]] = key_value[1]
        result["query_params"] = query_params
    
    return result