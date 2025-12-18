"""
QUESTION:
Generate a list of valid HTML tags used to structure content in a page, ordered based on their hierarchical relationships. Implement a function named `traverse_tree` that takes a tree node and a result list as parameters, and a function named `build_tree` that takes a tag as a parameter and returns a tree node. Ensure the algorithm has a time complexity of O(n) and space complexity of O(n), where n is the number of tags. Use a dictionary to map each tag to its parent tag.
"""

class TagNode:
    def __init__(self, name):
        self.name = name
        self.children = []

parent_map = {
    'html': None,
    'head': 'html',
    'title': 'head',
    'body': 'html',
    'h1': 'body',
    'p': 'body',
    # Add more tags and their parent tags here
}

def build_tree(tag):
    node = TagNode(tag)
    children = [child for child, parent in parent_map.items() if parent == tag]
    for child in children:
        node.children.append(build_tree(child))
    return node

def traverse_tree(node, result):
    result.append(node.name)
    for child in node.children:
        traverse_tree(child, result)