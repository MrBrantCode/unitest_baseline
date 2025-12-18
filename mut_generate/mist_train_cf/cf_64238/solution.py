"""
QUESTION:
Create a function 'text_to_html' that takes a string input, which may contain multiple lines, and returns the corresponding HTML string where each non-empty line is enclosed within paragraph tags ("<p>" and "</p>"). The function should ignore lines that only contain whitespace characters and not include them in the output.
"""

def text_to_html(text):
    # Split the text into lines
    lines = text.split('\n')
    # Add paragraph tags to each line and join them back together
    html = ''.join(f'<p>{line}</p>' for line in lines if line.strip())
    return html