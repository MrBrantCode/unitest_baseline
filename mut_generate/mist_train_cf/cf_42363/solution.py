"""
QUESTION:
Create a function `annotate_links_no_site(text, site)` that takes a string `text` and a string `site` as input, and returns the text with all URLs replaced by HTML anchor tags in the format `<a href="url">url</a>`, except for the URLs that belong to the `site` domain. The function should handle URLs in the form of `http://...`, `https://...`, or `www...`.
"""

import re

def annotate_links_no_site(text, site):
    pattern = r'(https?://\S+|www\.\S+)'
    annotated_text = text
    urls = re.findall(pattern, text)
    for url in urls:
        if site not in url:
            annotated_url = f'<a href="{url}">{url}</a>'
            annotated_text = annotated_text.replace(url, annotated_url)
    return annotated_text