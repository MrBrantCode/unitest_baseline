"""
QUESTION:
Create a function `process_url(request)` that takes a request as input, extracts the 'url' parameter, and returns the domain name of the URL if it is valid. If the 'url' parameter is not provided, return "Error: URL not provided in the request". If the URL is invalid, return "Error: Invalid URL format". The function should consider the standard URL structure and handle cases for 'www' subdomain and protocol (http or https).
"""

import re

def process_url(request):
    url = request.values.get('url', None)
    
    if url is None:
        return "Error: URL not provided in the request"
    
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  
        r'localhost|'  
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  
        r'(?::\d+)?'  
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    if re.match(url_pattern, url):
        domain = re.sub(r'^https?://', '', url)  
        domain = re.sub(r'^www\.', '', domain)  
        domain = domain.split('/')[0]  
        return domain
    else:
        return "Error: Invalid URL format"