"""
QUESTION:
Design the `encode` and `decode` methods for a URL shortening service. The `encode` method should take a long URL as input and return a unique short URL, and the `decode` method should take a short URL as input and return the original long URL. 

Constraints: 
- The `encode` method should produce unique short URLs for different long URLs. 
- The `decode` method should be able to decode short URLs even if the same long URL has been encoded multiple times. 
- The `encode` method should be able to handle long URLs of up to 1000 characters. 
- The `decode` method should return the original long URL even if it has been encoded multiple times. 
- The `encode` and `decode` methods should be able to handle at least 1 million calls each without significant performance degradation.
"""

def encode(longUrl: str) -> str:
    """Encodes a URL to a shortened URL."""
    return "http://tinyurl.com/" + str(hash(longUrl))

def decode(shortUrl: str, url_map: dict) -> str:
    """Decodes a shortened URL to the original URL."""
    return url_map.get(shortUrl)