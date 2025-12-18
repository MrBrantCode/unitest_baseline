"""
QUESTION:
Create a function `generate_html_tags` that generates a list of valid HTML tags used to structure content in a page, ordered hierarchically, with a time complexity of O(n) and a space complexity of O(n), where n is the number of tags. The function should take a dictionary mapping each tag to its parent tag as input and return the ordered list of tags. The tags should be ordered in a specific way based on their hierarchical relationships, with the root tag 'html' at the top of the hierarchy.
"""

class TagNode:
    def __init__(self, name):
        self.name = name
        self.children = []

def build_tree(tag, parent_map):
    node = TagNode(tag)
    children = [child for child, parent in parent_map.items() if parent == tag]
    for child in children:
        node.children.append(build_tree(child, parent_map))
    return node

def traverse_tree(node, result):
    result.append(node.name)
    for child in node.children:
        traverse_tree(child, result)

def generate_html_tags(parent_map):
    root = build_tree('html', parent_map)
    result = []
    traverse_tree(root, result)
    return result