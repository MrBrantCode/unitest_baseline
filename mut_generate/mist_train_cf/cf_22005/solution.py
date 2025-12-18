"""
QUESTION:
Create a function called `create_ordered_list` that takes two parameters: `items` (a list of strings) and `start` (an optional integer parameter with a default value of 1). The function should return a string of HTML code to create an ordered numbered list where each string in the input list is a separate list item. The function should properly handle special characters in the input strings and include the `start` attribute in the opening `<ol>` tag if provided.
"""

def create_ordered_list(items, start=1):
    html_code = f'<ol start="{start}">'
    for item in items:
        html_code += f'<li>{item}</li>'
    html_code += '</ol>'
    return html_code