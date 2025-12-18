"""
QUESTION:
Write a function `modify_html(html)` that modifies an HTML document by adding an "alt" attribute to all "img" tags without an existing "alt" attribute. If an "img" tag already has an "alt" attribute, the function should modify the value of the "alt" attribute to be the concatenation of the existing value and the word "modified". The function should return the modified HTML document as a string.
"""

def modify_html(html):
    # Split the HTML string into lines
    lines = html.split("\n")

    # Initialize a modified_lines list to store the modified lines
    modified_lines = []

    # Initialize a flag variable to keep track of whether we are inside an img tag
    inside_img_tag = False

    # Iterate over each line in the HTML
    for line in lines:
        # Check if the line contains an img tag
        if "<img" in line:
            # If it does, set the inside_img_tag flag to True
            inside_img_tag = True

            # Check if the img tag already has an alt attribute
            if 'alt="' in line:
                # If it does, modify the value of the alt attribute
                line = line.replace('alt="', 'alt="modified ')

        # Check if the line is the closing tag of an img tag
        if "</img>" in line or "/>" in line:
            # If it is, set the inside_img_tag flag to False
            inside_img_tag = False

        # Check if we are inside an img tag without an alt attribute
        if inside_img_tag and 'alt="' not in line:
            # If we are, add an empty alt attribute to the img tag
            line = line.replace("<img", '<img alt=""')

        # Add the modified line to the modified_lines list
        modified_lines.append(line)

    # Join the modified_lines list back into a single string
    modified_html = "\n".join(modified_lines)

    return modified_html