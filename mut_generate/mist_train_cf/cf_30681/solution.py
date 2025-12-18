"""
QUESTION:
Implement the function `extract_social_media_urls(html_code)` that takes a string `html_code` as input and returns a dictionary containing social media platform names as keys and their respective URLs as values. The input string is an HTML code snippet containing embedded image tags and corresponding URLs for social media platforms. The function should use the text within the `img` tags to determine the platform names and the corresponding URLs from the subsequent lines of the input string. The platform names in the dictionary should be as they appear in the input string (e.g., 'GitHub', 'LinkedIn', 'Instagram').
"""

import re

def extract_social_media_urls(html_code: str) -> dict:
    img_tags = re.findall(r'<img.*?src="(.*?)".*?\/>(?:\[(.*?)\])', html_code)
    url_tags = re.findall(r'\[(.*?)\]:\s(.*?)\n', html_code)
    
    platform_urls = {}
    for img_tag in img_tags:
        platform_name = img_tag[1]
        platform_url = [url[1] for url in url_tags if url[0].lower() == platform_name.lower()]
        if platform_url:
            platform_urls[platform_name] = platform_url[0]
    
    return platform_urls