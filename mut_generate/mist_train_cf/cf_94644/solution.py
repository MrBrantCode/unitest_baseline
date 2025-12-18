"""
QUESTION:
Write a function named `generate_html_document` that takes four parameters: `title`, `heading`, `body`, and `footer`. The function should generate a complete HTML document with the given parameters. The generated HTML document should adhere to the following constraints:
- The `title` tag should have a maximum length of 50 characters. If the `title` exceeds this length, truncate it to 50 characters and append an ellipsis.
- The `heading` tag should have a maximum length of 100 characters. If the `heading` exceeds this length, truncate it to 100 characters and append an ellipsis.
- The `body` tag should have a maximum length of 500 characters. If the `body` exceeds this length, truncate it to 500 characters and append an ellipsis.
- The HTML document should include a `footer` tag with the given `footer` text.
- The HTML document should have a maximum size of 2KB. If the generated HTML document exceeds this size, raise an exception.

The function should return the generated HTML document as a string.
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