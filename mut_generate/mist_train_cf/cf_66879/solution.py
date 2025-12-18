"""
QUESTION:
Identify the abstract data type employed in the given procedural algorithm. The algorithm uses a data structure with `isEmpty()` and `pop()` operations. Determine the specific type of data structure used, given that it follows a specific principle for adding and removing elements.
"""

def entrance(stack):
    if stack.isEmpty():
        return False
    return stack.pop()