"""
QUESTION:
Implement a function `is_html_tags_correct(tags)` that takes in a list of strings representing HTML tags and returns True if the tags are structured correctly based on their hierarchical relationships. The function should optimize both time complexity and space complexity.

The function should check for the following hierarchical relationships:
- An opening tag must be closed by a corresponding closing tag.
- Opening and closing tags must be nested correctly, with each opening tag being closed before any tags inside it are closed.

Assume that the input list contains only valid HTML tags, with opening tags starting with "<" and ending with ">" and closing tags starting with "</" and ending with ">".
"""

def is_html_tags_correct(tags):
    stack = []
    
    for tag in tags:
        if tag.startswith("<"):
            if tag.startswith("</"): # Closing tag
                if len(stack) == 0:
                    return False
                
                if tag[2:-1] != stack[-1]:
                    return False
                
                stack.pop()
            else: # Opening tag
                stack.append(tag[1:-1])
    
    return len(stack) == 0