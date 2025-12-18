"""
QUESTION:
Write a function called `count_div_tags` that takes a string of HTML code as input and returns the number of div tags present in the code. The function should count both opening and closing div tags, but only return the total count of unique div tags. The input string can contain nested div tags and other HTML elements.
"""

def count_div_tags(html_code):
    count = 0
    start_tag = "<div"
    end_tag = "</div>"
    i = 0
    while i < len(html_code):
        if html_code[i:i+len(start_tag)] == start_tag:
            count += 1
            i += len(start_tag)
        elif html_code[i:i+len(end_tag)] == end_tag:
            i += len(end_tag)
        else:
            i += 1
    return count