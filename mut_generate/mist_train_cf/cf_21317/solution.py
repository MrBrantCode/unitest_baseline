"""
QUESTION:
Write a function called `extract_city_name` that takes a URL as input and returns the city name extracted from the URL. The city name is the last non-empty path segment in the URL, where underscores are replaced with spaces and the first letter is capitalized. The function should handle URLs with or without the "www" prefix, different formats and variations, query parameters, fragments, special characters, and non-English city names.
"""

import urllib.parse

def extract_city_name(url):
    parsed_url = urllib.parse.urlparse(url)
    path_segments = parsed_url.path.split('/')
    city_name = None
    for segment in reversed(path_segments):
        if segment:
            city_name = segment.replace('_', ' ')
            break
    if city_name:
        return city_name.capitalize()
    else:
        return None