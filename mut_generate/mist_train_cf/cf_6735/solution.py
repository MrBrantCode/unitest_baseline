"""
QUESTION:
Write a function named `extract_city_name` that takes a URL string as input and returns the city name. The city name is the path segment that contains an underscore, and it should be extracted regardless of its position in the URL. The function should handle URLs with multiple segments, query parameters, and fragments, and it should replace underscores with spaces in the city name. The city name should maintain its original capitalization and should be able to contain special characters and non-English characters.
"""

import urllib.parse

def extract_city_name(url):
    # Parse the URL to extract the path
    parsed_url = urllib.parse.urlparse(url)
    path = parsed_url.path

    # Remove any leading or trailing slashes
    path = path.strip('/')

    # Split the path into segments
    segments = path.split('/')

    # Find the segment that contains the city name
    city_segment = None
    for segment in segments:
        if '_' in segment:
            city_segment = segment
            break

    # Extract the city name from the segment
    if city_segment:
        city_name = city_segment.replace('_', ' ')
        return city_name

    return None