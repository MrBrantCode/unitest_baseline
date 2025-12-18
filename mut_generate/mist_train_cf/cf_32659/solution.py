"""
QUESTION:
Implement the `validateAspectRatio` function that takes a string `aspectRatio` representing the aspect ratio of a video in the form "width:height" and returns a boolean value indicating whether the aspect ratio is supported or not. The aspect ratio is supported if both width and height are positive integers and the width is at least 640 pixels and the height is at least 480 pixels. The function should also handle cases where the input format is incorrect or does not match the expected "width:height" format.
"""

import re

def validateAspectRatio(aspectRatio):
    pattern = r'^(\d+):(\d+)$'
    match = re.match(pattern, aspectRatio)
    if match:
        width = int(match.group(1))
        height = int(match.group(2))
        if width >= 640 and height >= 480:
            return True
    return False