"""
QUESTION:
Implement a function `findTagPosition(html, tag)` that finds the position of a specific HTML tag within a given HTML document. The function takes two parameters: `html`, a string representing the HTML document, and `tag`, a string representing the HTML tag to be located. The function returns a tuple `(line, index)` representing the line number and character index of the start of the specified tag within the HTML document. If the tag is not found, the function returns `-1, -1`.
"""

def entance(html, tag):
    lines = html.split('\n')
    current_line = 1
    current_index = 0

    for line in lines:
        index = line.find(tag)
        if index != -1:
            return current_line, index
        current_line += 1
        current_index += len(line) + 1  

    return -1, -1 