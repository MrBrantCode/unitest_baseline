"""
QUESTION:
Write a function `extractUrls(html)` that takes a string `html` representing the content of an HTML file as input and returns a dictionary containing the count of unique URLs for CSS files and background images. The function should consider both the `href` attribute in the `<link>` tag for CSS files and the `url()` function in inline styles for background images. The HTML content is assumed to be well-formed, with URLs enclosed in double quotes and following the specified format.
"""

import re

def extractUrls(html):
    css_urls = set(re.findall(r'href="([^"]+\.css)"', html))
    background_image_urls = set(re.findall(r'url\(([^)]+)\)', html))

    return {
        "css": len(css_urls),
        "background_images": len(background_image_urls)
    }