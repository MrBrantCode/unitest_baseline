"""
QUESTION:
Create a function `processHTML` that takes in an HTML snippet as a string. Extract the URL from the anchor tag with class "btn btn-orange-general view-all hidden-xs" and store it in a variable. Then, modify the class attribute of the div tag with class "col-sm-offset-4 col-sm-4 text-center" to "modified-class". The input HTML snippet will always contain the specified anchor and div tags with the given classes. Return the modified HTML snippet.
"""

import re

def processHTML(html_snippet):
    # Extract the URL from the anchor tag
    url_match = re.search(r'<a class="btn btn-orange-general view-all hidden-xs" href="([^"]+)">', html_snippet)
    if url_match:
        url = url_match.group(1)
    else:
        return "Invalid HTML snippet"

    # Modify the class attribute of the div tag
    modified_html = re.sub(r'<div class="col-sm-offset-4 col-sm-4 text-center">', 
                           '<div class="col-sm-offset-4 col-sm-4 text-center modified-class">', 
                           html_snippet)

    return modified_html