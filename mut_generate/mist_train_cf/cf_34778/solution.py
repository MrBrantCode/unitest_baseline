"""
QUESTION:
Implement the `sort_colors` function, which takes a list of colors as input and returns a new list with the colors sorted in the following order: "red", "green", "blue", "yellow", "orange", "purple", "black", "white", and any other colors in alphabetical order. The function should maintain the same order of duplicates as the input list.
"""

from typing import List

def sort_colors(colors: List[str]) -> List[str]:
    color_order = ["red", "green", "blue", "yellow", "orange", "purple", "black", "white"]
    color_count = {color: i for i, color in enumerate(color_order)}
    
    def custom_sort(color):
        if color in color_count:
            return (color_count[color], color)
        else:
            return (len(color_order), color)
    
    return sorted(colors, key=custom_sort)