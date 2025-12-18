"""
QUESTION:
Write a function called `extract_img_tags_and_alt_text` that takes an HTML file content as a string and returns a list of tuples, where each tuple contains the source URL and alt text of an image. The function should parse the HTML content manually without using any HTML parsing libraries or frameworks.
"""

import re

def extract_img_tags_and_alt_text(html_content):
    """
    Extracts image source URLs and alt text from an HTML content string.

    Args:
        html_content (str): The input HTML content as a string.

    Returns:
        list: A list of tuples, where each tuple contains the source URL and alt text of an image.
    """

    # Find all occurrences of <img> tags in the HTML content
    img_tags = re.findall(r'<img\s[^>]*>', html_content)

    # Initialize an empty list to store the image source URLs and alt text
    images = []

    # Parse the src and alt attributes from each <img> tag
    for img_tag in img_tags:
        src_match = re.search(r'src="([^"]+)"', img_tag)
        alt_match = re.search(r'alt="([^"]+)"', img_tag)

        src = src_match.group(1) if src_match else ""
        alt = alt_match.group(1) if alt_match else "[No Alt Text]"

        # Append the image source URL and alt text to the list
        images.append((src, alt))

    return images