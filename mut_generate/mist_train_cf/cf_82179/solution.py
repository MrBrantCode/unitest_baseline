"""
QUESTION:
Create a function `html_to_plain_text(html_code)` that takes a string of HTML content as input and returns a string of plain text. The function should not use any libraries and should exclude HTML tags from the output. It should only work for simple HTML strings without attributes, nested tags, comments, scripts, or styles.
"""

def html_to_plain_text(html_code):
    """
    This Function will convert HTML to Plain Text
    :param html_code: string
    :return: string
    """
    text = ""
    record = False
    for char in html_code:
        if char == '<':
            record = False
        elif char == '>':
            record = True
        elif record:
            text += char
    return text