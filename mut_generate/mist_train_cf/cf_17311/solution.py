"""
QUESTION:
Write a function `generate_html_document(title, heading, body, footer)` that generates a complete HTML document. The function should truncate the title if it exceeds 50 characters, the heading if it exceeds 100 characters, and the body if it exceeds 500 characters. The function should also include a footer tag with the provided footer text. The generated HTML document should not exceed 2KB in size.
"""

def generate_html_document(title, heading, body, footer):
    # Check if title length exceeds the maximum allowed length
    if len(title) > 50:
        title = title[:47] + '...'

    # Check if heading length exceeds the maximum allowed length
    if len(heading) > 100:
        heading = heading[:97] + '...'

    # Check if body length exceeds the maximum allowed length
    if len(body) > 500:
        body = body[:497] + '...'

    # Create the HTML document
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{heading}</h1>
        <p>{body}</p>
        <footer>{footer}</footer>
    </body>
    </html>
    '''

    # Check if the HTML document size exceeds the maximum allowed size
    if len(html) > 2048:
        raise Exception("Generated HTML document exceeds the maximum allowed size of 2KB.")

    return html