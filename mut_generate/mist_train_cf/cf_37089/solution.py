"""
QUESTION:
Implement a function called `sort_colors` that takes a dictionary `log_colors` representing log levels and their corresponding colors as RGB values, and returns a new dictionary with the colors sorted in ascending order based on their RGB values. If two colors have the same RGB values, they should be sorted alphabetically based on their log level names. The input and output dictionary should have string keys (log levels) and tuple values (RGB colors).
"""

def sort_colors(log_colors: dict) -> dict:
    sorted_colors = sorted(log_colors.items(), key=lambda x: (x[1], x[0]))
    return {k: v for k, v in sorted_colors}