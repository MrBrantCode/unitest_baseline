"""
QUESTION:
Write a function `extract_information` that takes a string `html_content` as input and returns a tuple containing two values: an integer representing the number of GitHub stars and a string representing the welcome message. The function should extract the GitHub stars from the `<gh_stars>` tag and the welcome message from the `<span>` tag with the style attribute `color:#fff;`. If the tags are not found, the function should return 0 for the GitHub stars and an empty string for the welcome message.
"""

import re

def extract_information(html_content: str) -> (int, str):
    # Extract GitHub stars
    stars_match = re.search(r'<gh_stars>(\d+)', html_content)
    stars = int(stars_match.group(1)) if stars_match else 0
    
    # Extract welcome message
    message_match = re.search(r'<span style="color:#fff;">(.*?)&nbsp;</span>', html_content)
    message = message_match.group(1) if message_match else ""
    
    return stars, message