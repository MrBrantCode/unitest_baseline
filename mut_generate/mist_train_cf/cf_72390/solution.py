"""
QUESTION:
Write a Python function, `shorten_url`, to shorten a given URL and another function, `reverse_shorten_url`, to reverse the shortened URL back to its original form. The shortened URL should be in the format "http://shorturl.com/encoded_url". Use base64 encoding and decoding to achieve this. The `shorten_url` function should take a URL as input and return the shortened URL, and the `reverse_shorten_url` function should take a shortened URL as input and return the original URL.
"""

import base64

# Function to shorten a URL
def shorten_url(url):
    """Shorten a given URL using base64 encoding."""
    encoded_url = base64.b64encode(url.encode("utf-8"))
    return "http://shorturl.com/" + str(encoded_url, 'utf-8')

# Function to reverse a shortened URL
def reverse_shorten_url(short_url):
    """Reverse a shortened URL back to its original form using base64 decoding."""
    encoded_url = short_url.replace("http://shorturl.com/", "")
    decoded_url = base64.b64decode(encoded_url)
    return str(decoded_url, 'utf-8')