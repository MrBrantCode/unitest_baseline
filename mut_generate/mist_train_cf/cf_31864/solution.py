"""
QUESTION:
Create a function `extractImageUrls(html: str) -> List[str]` that takes a string `html` of length between 1 and 10^4, representing HTML content, and returns a list of strings representing the URLs of images present in the HTML string. The image URLs are in the format `<img src='url' ...>`, where `url` is the URL of the image.
"""

from typing import List
import re

def extractImageUrls(html: str) -> List[str]:
    img_urls = re.findall(r"<img[^>]*?src=['\"](.*?)['\"][^>]*?>", html)
    return img_urls