"""
QUESTION:
Create a function `maxNestingLevel(html)` that takes a string `html` representing the HTML code without line breaks or additional spaces and returns the maximum nesting level of the HTML elements. The nesting level of an element is determined by the number of its ancestor elements, and the nesting level starts at 1 for the outermost element.
"""

def max_nesting_level(html):
    max_level = 0
    current_level = 0
    for char in html:
        if char == '<':
            current_level += 1
            max_level = max(max_level, current_level)
        elif char == '>':
            current_level -= 1
    return max_level