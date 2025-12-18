"""
QUESTION:
Create a function `style_text` that takes a string `text` as input and returns the text with its color changed to blue and font size increased to 20px. The function should return the styled text in HTML format using the `<span>` tag.
"""

def style_text(text):
    return '<span style="color:blue; font-size:20px;">' + text + '</span>'