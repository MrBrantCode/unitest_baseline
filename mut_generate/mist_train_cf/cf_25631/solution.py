"""
QUESTION:
Write a function `createList` that takes a list of strings as input and returns a string representing the HTML of an unordered list containing each string as a list item.
"""

def createList(strings):
    html = "<ul>\n"
    for string in strings:
        html += f"<li>{string}</li>\n"
    html += "</ul>"
    return html