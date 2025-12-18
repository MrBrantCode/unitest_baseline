"""
QUESTION:
Write a function named `add_paragraph` that takes in two parameters: a string of valid HTML code and a string of text. The function should find the first occurrence of a div element with a class of "example" and add a paragraph element containing the given text as the last child of the div element, without modifying the original indentation. If no div element with a class of "example" exists, the original HTML string should be returned.
"""

def add_paragraph(html, text):
    # Find the index of the first occurrence of '<div class="example">'
    start_index = html.find('<div class="example">')
    
    # If no div element with a class of "example" exists, return the original HTML string
    if start_index == -1:
        return html
    
    # Find the index of the closing tag '</div>'
    end_index = html.find('</div>', start_index) + len('</div>')
    
    # Insert the paragraph element after the opening tag
    modified_html = html[:end_index - len('</div>')] + '\n<p>' + text + '</p></div>'
    
    return modified_html