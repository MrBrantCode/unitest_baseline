"""
QUESTION:
Create a function named `get_url_info` that takes a string URL as input. The function should return a tuple containing the URL's protocol (either 'http' or 'https') and its domain type (e.g., 'com', 'org', 'edu', etc.). The function should also detect potential phishing sites by scanning the URL for common red flags such as the presence of 'http' in an 'https' URL, long URLs, and URLs containing '@'. If the URL is invalid (does not contain a scheme and a network location), the function should raise an exception.
"""

from urllib.parse import urlparse
import re

def get_url_info(url):
    """
    This function takes a string URL as input and returns a tuple containing 
    the URL's protocol (either 'http' or 'https') and its domain type.
    
    It also detects potential phishing sites by scanning the URL for common 
    red flags such as the presence of 'http' in an 'https' URL, long URLs, 
    and URLs containing '@'. If the URL is invalid, the function raises an exception.
    
    Parameters:
    url (str): The URL to be processed.
    
    Returns:
    tuple: A tuple containing the URL's protocol and its domain type.
    """
    
    # Check if the URL is valid
    try:
        result = urlparse(url)
        if not result.scheme or not result.netloc or result.scheme not in ['https', 'http']:
            raise Exception("Invalid URL")
    except:
        raise Exception("Invalid URL")

    # Detect phishing
    if url.startswith('https') and 'http' in url[5:]:
        print('Warning: This URL has characteristics common to phishing attacks. Proceed with caution.')
    if len(url) > 75:
        print('Warning: This URL has characteristics common to phishing attacks. Proceed with caution.')
    if re.search('@', url):
        print('Warning: This URL has characteristics common to phishing attacks. Proceed with caution.')

    # Return the URL's protocol and domain type
    return result.scheme, result.netloc.split('.')[-1]