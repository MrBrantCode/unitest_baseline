"""
QUESTION:
Implement a function `is_html_tags_correct(tags)` that takes a list of strings representing HTML tags and returns True if the tags are structured correctly based on their hierarchical relationships. The function should optimize both time complexity and space complexity. The tags will always be valid HTML structures with opening and closing tags in the correct order, and will start and end with the corresponding brackets.
"""

def is_html_tags_correct(tags):
    stack = []
    
    for tag in tags:
        if tag.startswith("<"):
            if tag.startswith("</"): 
                if len(stack) == 0:
                    return False
                
                if tag[2:-1] != stack[-1]:
                    return False
                
                stack.pop()
            else: 
                stack.append(tag[1:-1])
    
    return len(stack) == 0