"""
QUESTION:
Write a function called `modify_html` that takes a string representation of an HTML document as input. The function should modify the document by adding an "alt" attribute to all "img" tags without an existing "alt" attribute. If an "img" tag already has an "alt" attribute, the function should modify the value of the "alt" attribute to be the concatenation of the existing value and the word "modified". The function should return the modified HTML document. The input HTML document can be a multi-line string and can contain any number of "img" tags with or without "alt" attributes.
"""

def modify_html(html):
    lines = html.split("\n")
    modified_lines = []
    inside_img_tag = False

    for line in lines:
        if "<img" in line:
            inside_img_tag = True
            if 'alt="' in line:
                line = line.replace('alt="', 'alt="modified ')

        if "</img>" in line or "/>" in line:
            inside_img_tag = False

        if inside_img_tag and 'alt="' not in line:
            line = line.replace("<img", '<img alt=""')

        modified_lines.append(line)

    modified_html = "\n".join(modified_lines)
    return modified_html