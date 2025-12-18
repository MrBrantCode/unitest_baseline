"""
QUESTION:
Create a Python function `validate_urls` that takes a dictionary `valid_urls_dict` and a list `valid_locations` as parameters. The dictionary contains keys representing server addresses and ports, with corresponding values being lists of URLs. The list contains the expected valid URLs for each server address and port combination. The function should return `True` if all the URLs in the dictionary match the expected valid URLs, and `False` otherwise.
"""

def validate_urls(valid_urls_dict: dict, valid_locations: list) -> bool:
    for urls in valid_urls_dict.values():
        for url in urls:
            if url not in valid_locations:
                return False
    return True