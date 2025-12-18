"""
QUESTION:
Implement a `build_dom_tree` function that converts a given string of HTML into a DOM tree using recursion. The function should ensure each HTML tag is properly closed and nested within its parent tag, and it should also validate for any syntax errors or missing closing tags in the HTML string. The function should return the root node of the DOM tree if the HTML string is valid, or `None` if there are any syntax errors.
"""

class Node:
    def __init__(self, tag):
        self.tag = tag
        self.children = []

def build_dom_tree(html_string):
    stack = []
    root = None

    i = 0
    while i < len(html_string):
        if html_string[i] == '<':
            if html_string[i:i+2] == '</':
                i += 2
                tag_end_index = html_string.find('>', i)
                tag_name = html_string[i:tag_end_index]
                i = tag_end_index + 1

                current_node = stack.pop()
                if current_node.tag != tag_name:
                    print("Syntax Error: Invalid closing tag:", tag_name)
                    return None
            else:
                i += 1
                tag_end_index = html_string.find('>', i)
                tag_name = html_string[i:tag_end_index]
                i = tag_end_index + 1

                new_node = Node(tag_name)
                if not root:
                    root = new_node
                if stack:
                    stack[-1].children.append(new_node)
                stack.append(new_node)
        else:
            text_end_index = html_string.find('<', i)
            text_content = html_string[i:text_end_index].strip()
            i = text_end_index

            if text_content:
                current_node = stack[-1]
                current_node.children.append(text_content)

    if stack:
        print("Syntax Error: Missing closing tag for", stack[-1].tag)
        return None

    return root