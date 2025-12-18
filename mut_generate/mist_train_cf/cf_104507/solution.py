"""
QUESTION:
Write a function named `parse_url` that takes a URL as input and returns a tuple containing the server name in uppercase and the username. The function should correctly handle URLs in the format "https://server_name/path/to/username" and extract the server name from the domain and the username from the last part of the path.
"""

import urllib.parse

def parse_url(url):
    """
    This function takes a URL as input and returns a tuple containing the server name in uppercase and the username.
    
    Parameters:
    url (str): The URL to be parsed.
    
    Returns:
    tuple: A tuple containing the server name in uppercase and the username.
    """
    
    # Parse the URL
    parsed_url = urllib.parse.urlparse(url)
    
    # Extract the server name and username
    server_name = parsed_url.netloc
    username = parsed_url.path.split("/")[-1]
    
    # Convert the server name to uppercase
    server_name = server_name.upper()
    
    return (server_name, username)