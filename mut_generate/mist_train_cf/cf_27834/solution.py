"""
QUESTION:
Write a function `count_html_tags` that takes an HTML snippet as input and returns a dictionary containing the count of each unique tag name present in the snippet. The function should count both opening and closing tags separately and ignore any text content within the tags. Each tag name should be counted as a unique key in the output dictionary, and its corresponding value should be the total count of that tag in the snippet.
"""

def count_html_tags(html_snippet):
    tag_counts = {}
    current_tag = ""
    in_tag = False

    for char in html_snippet:
        if char == "<":
            in_tag = True
            current_tag = ""
        elif char == ">":
            in_tag = False
            if current_tag.startswith("/"):
                tag_name = current_tag[1:]
                if tag_name in tag_counts:
                    tag_counts[tag_name] += 1
                else:
                    tag_counts[tag_name] = 1
            else:
                tag_name = current_tag.split(" ")[0]
                if tag_name in tag_counts:
                    tag_counts[tag_name] += 1
                else:
                    tag_counts[tag_name] = 1
        elif in_tag:
            current_tag += char

    return tag_counts