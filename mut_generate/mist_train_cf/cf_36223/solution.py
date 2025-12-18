"""
QUESTION:
Create a function named `extract_captcha_value` that takes a URL as input and returns the extracted captcha value as a string. The URL is in the format `https://example.com/captcha/{captcha_value}.png`, where `{captcha_value}` is the actual captcha value that needs to be extracted. The captcha value consists of alphanumeric characters.
"""

import re

def extract_captcha_value(url):
    # Using regular expression to extract the captcha value from the URL
    pattern = r"https://example.com/captcha/(\w+)\.png"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return "Captcha value not found"