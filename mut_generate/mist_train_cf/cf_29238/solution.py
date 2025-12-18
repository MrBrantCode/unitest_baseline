"""
QUESTION:
Write a function called `is_valid_live_russia_tv_url` that takes a single string parameter `url` and returns a boolean value indicating whether the URL is valid for Live Russia TV. The function should adhere to the following rules:
- The URL should start with "https://live.russia.tv/index/index/channel_id/" followed by a positive integer.
- The integer after "channel_id/" can range from 1 to 999, inclusive.
"""

import re

def is_valid_live_russia_tv_url(url: str) -> bool:
    pattern = r'^https://live\.russia\.tv/index/index/channel_id/([1-9]\d{0,2})$'
    return bool(re.match(pattern, url))