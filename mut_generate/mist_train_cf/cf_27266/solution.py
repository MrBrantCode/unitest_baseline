"""
QUESTION:
Implement a function `encode_url(value)` that takes a string representing a URL as input, splits it by '/', and returns the second last segment if it exists. If the input URL has fewer than two segments, the function should return an empty string.
"""

def encode_url(value):
    segments = value.split('/')
    if len(segments) >= 2:
        return segments[-2]
    else:
        return ""