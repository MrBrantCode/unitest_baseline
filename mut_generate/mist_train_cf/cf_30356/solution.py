"""
QUESTION:
Implement a function `convert_to_ascii_art(image)` that takes a 2D array `image` of grayscale pixel values (ranging from 0 to 255) and returns a string representing the colored ASCII art. Use the following mapping to convert grayscale pixel values to ASCII characters and colors:
- Grayscale pixel value 0-51: Use the character "@" with color yellow
- Grayscale pixel value 52-102: Use the character "#" with color green
- Grayscale pixel value 103-153: Use the character "%" with color cyan
- Grayscale pixel value 154-204: Use the character "&" with color blue
- Grayscale pixel value 205-255: Use the character "*" with color magenta

Assume that the input grayscale image is a rectangular 2D array with dimensions m x n. The output should maintain the aspect ratio of the input image.
"""

def convert_to_ascii_art(image):
    ascii_art = ""
    for row in image:
        for pixel in row:
            if pixel <= 51:
                ascii_art += "\033[93m@"  # Yellow
            elif pixel <= 102:
                ascii_art += "\033[92m#"  # Green
            elif pixel <= 153:
                ascii_art += "\033[96m%"  # Cyan
            elif pixel <= 204:
                ascii_art += "\033[94m&"  # Blue
            else:
                ascii_art += "\033[95m*"  # Magenta
        ascii_art += "\033[0m\n"  # Reset color
    return ascii_art