"""
QUESTION:
Implement a function named `remove_comments` that takes a string of HTML content as input and returns the content with all HTML comments removed, while preserving the original formatting and structure. The function should use recursion to traverse the HTML structure and identify and remove comment nodes, without relying on built-in HTML parsing libraries or regular expressions.
"""

def remove_comments(html):
    result = ''
    i = 0
    while i < len(html):
        if html[i:i+4] == '<!--':
            # Find the end of the comment
            end_index = html.find('-->', i+4)
            if end_index != -1:
                i = end_index + 3  # Skip the comment closing tag
            else:
                # If the end of the comment is not found, consider it as a regular text
                result += html[i]
                i += 1
        else:
            if html[i] == '<':
                # Find the end of the tag
                end_index = html.find('>', i+1)
                if end_index != -1:
                    result += html[i:end_index+1]  # Add the tag to the result
                    i = end_index + 1
                else:
                    # If the end of the tag is not found, consider it as a regular text
                    result += html[i]
                    i += 1
            else:
                result += html[i]  # Add regular text to the result
                i += 1

    return result