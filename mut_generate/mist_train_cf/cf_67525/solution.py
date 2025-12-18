"""
QUESTION:
Write a function called `construct_url` that constructs a URL given the following components: protocol, subdomain, domain, path, query parameters, and fragment identifier. The function should handle various protocols, multiple subdomains, and optional query parameters and fragment identifier. It should also properly encode special or reserved characters in the URL components and follow the RFC 3986 URI syntax standard. The function should return the constructed URL. The protocol, subdomain, domain, path, query parameters, and fragment identifier should be passed as separate arguments to the function. The query parameters should be a dictionary of key-value pairs.
"""

from urllib.parse import urlencode, quote, quote_plus, urlunparse

def construct_url(protocol, subdomain, domain, path, query_params, fragment):
    # encode special/reserved characters
    subdomain = quote(subdomain.encode('utf-8'), safe=':/@')
    domain = quote(domain.encode('utf-8'), safe=':/@')
    path = quote(path.encode('utf-8'), safe=':/@')
    
    # include subdomain in netloc if it's not vacant
    netloc = domain
    if subdomain != '':
        netloc = '%s.%s' % (subdomain, domain)
    
    # parse the query parameters
    query = urlencode(query_params, quote_via=quote_plus)
    
    # construct the url
    url = urlunparse((protocol, netloc, path, '', query, fragment))
    return url