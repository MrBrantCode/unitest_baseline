"""
QUESTION:
Write a function `extract_city_name` that takes a URL string as input and returns the city name. The city name can consist of multiple words separated by underscores and is case-sensitive. The function should handle URLs with different formats and variations, such as "https://example.com/los_angeles", "https://www.example.com/new_york", or "https://example.com/city/paris".
"""

import re

def extract_city_name(url):
    # Remove any trailing slashes from the URL
    url = url.rstrip('/')
    
    # Remove the "https://" or "http://" prefix from the URL
    url = re.sub(r'^https?://', '', url)
    
    # Remove the "www" prefix from the URL if present
    url = url.replace('www.', '')
    
    # Split the URL by '/' and get the last segment
    segments = url.split('/')
    city_name = segments[-1]
    
    # Replace underscores with spaces in the city name
    city_name = city_name.replace('_', ' ')
    
    return city_name