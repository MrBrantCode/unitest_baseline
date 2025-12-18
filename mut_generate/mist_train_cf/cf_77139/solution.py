"""
QUESTION:
Write a function `analyze_url(url)` that takes a URL string as input and returns a dictionary containing the URL's components. The function should validate the URL and identify its protocol, domain name, path, parameters, and port (if available). The function should consider a URL as valid if it has both a scheme (e.g., HTTP, HTTPS, FTP) and a network location. If the URL is invalid, the function should return a dictionary with 'VALID' set to 'No'. The function should handle URLs with international characters and special encodings like percent encoding.
"""

from urllib.parse import urlparse, parse_qs

def analyze_url(url):
    results = urlparse(url)
    url_data = {'URL': url}
    
    if results.scheme and results.netloc:
        url_data['VALID'] = 'Yes'
    else:
        url_data['VALID'] = 'No'
        return url_data

    url_data['PROTOCOL'] = results.scheme
    url_data['DOMAIN_NAME'] = results.hostname

    if results.port:
        url_data['PORT'] = results.port
    
    url_data['PATH'] = results.path if results.path else 'No'
    
    url_data['PARAMETERS'] = parse_qs(results.query) if results.query else 'No'

    return url_data