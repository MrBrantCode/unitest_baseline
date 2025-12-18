"""
QUESTION:
Implement a function named `generate_breadcrumb` that takes a URL as input and returns the breadcrumb navigation HTML code as a string. The breadcrumb should display the hierarchy of the pages leading to the current page. The function should split the URL into segments, remove empty segments and the domain part, and generate the breadcrumb HTML with each segment as a clickable link to its respective page.
"""

def generate_breadcrumb(url):
    # Split the URL path into segments
    segments = url.split('/')
    
    # Remove empty segments and the domain part
    segments = [segment for segment in segments if segment]
    segments = segments[2:]  # Remove the domain part
    
    # Generate the breadcrumb HTML
    breadcrumb_html = '<ul class="breadcrumb">'
    breadcrumb_html += '<li class="breadcrumb-item"><a href="/">Home</a></li>'  # Home link
    
    # Iterate through the URL segments to create breadcrumb links
    path_so_far = ''
    for segment in segments:
        path_so_far += '/' + segment
        breadcrumb_html += f'<li class="breadcrumb-item"><a href="{path_so_far}">{segment.capitalize()}</a></li>'
    
    breadcrumb_html += '</ul>'
    
    return breadcrumb_html