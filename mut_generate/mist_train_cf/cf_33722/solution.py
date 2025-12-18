"""
QUESTION:
Implement a function `extract_video_id` that takes a string `video_url` as input and returns the extracted video ID from the URL. The input URL should be in the format "https://video.dtu.dk/media/*/*" where * represents any characters. The video ID is the last part of the URL path and consists of alphanumeric characters and underscores. The function should validate the input URL format and raise an error if it's invalid. The video ID should be returned as a string.
"""

import re

def extract_video_id(video_url: str) -> str:
    # Regular expression pattern to match the video ID
    pattern = r'/(\w+)$'
    
    # Validate the input URL format
    assert video_url.startswith("https://video.dtu.dk/"), "Invalid video.dtu.dk URL"
    
    # Extract the video ID using the regular expression pattern
    match = re.search(pattern, video_url)
    assert match, "Video ID not found in the URL"
    
    return match.group(1)