"""
QUESTION:
Implement a function `parseColor` that takes a string as input, representing a code snippet containing a comment that describes a color in either RGB or named format. The function should return the color information in a standardized format: a tuple of three integers for RGB format or the name of the color in lowercase for named format. The input string will always contain a comment in the format `// R G B colorName` for RGB or `// colorName` for named format, where RGB values are integers in the range 0 to 255 and color names may contain multiple words separated by spaces.
"""

from typing import Union, Tuple

def parseColor(code: str) -> Union[Tuple[int, int, int], str]:
    comment_start = code.find('//')  
    if comment_start != -1:
        comment = code[comment_start + 2:]  
        parts = comment.split()  
        if len(parts) >= 3 and all(part.isdigit() for part in parts[:3]):
            rgb_values = tuple(int(part) for part in parts[:3])
            return rgb_values
        else:
            color_name = ' '.join(parts).lower()
            return color_name
    return ''  