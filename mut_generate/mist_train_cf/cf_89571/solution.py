"""
QUESTION:
Write a function `extract_city_name(url)` that takes a URL string as input and returns the city name extracted from the URL. The city name is the path segment that contains at least one underscore and can consist of multiple words separated by underscores. The function should handle URLs with different formats and variations, such as multiple segments before the city name, with or without the "www" prefix, query parameters, and fragments. The city name should maintain its original capitalization and can contain special characters or non-English characters.
"""

import urllib.parse

def extract_city_name(url):
    """
    Extracts the city name from a given URL.
    
    The city name is the path segment that contains at least one underscore and can consist of multiple words separated by underscores.
    
    Args:
        url (str): The URL string to extract the city name from.
    
    Returns:
        str: The extracted city name or None if not found.
    """
    # Parse the URL to extract the path
    parsed_url = urllib.parse.urlparse(url)
    path = parsed_url.path

    # Remove any leading or trailing slashes
    path = path.strip('/')

    # Split the path into segments
    segments = path.split('/')

    # Find the segment that contains the city name
    city_segment = next((segment for segment in segments if '_' in segment), None)

    # Extract the city name from the segment
    if city_segment:
        city_name = city_segment.replace('_', ' ')
        return city_name

    return None