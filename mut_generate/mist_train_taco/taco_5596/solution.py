"""
QUESTION:
# Task
 You are implementing your own HTML editor. To make it more comfortable for developers you would like to add an auto-completion feature to it.

 Given the starting HTML tag, find the appropriate end tag which your editor should propose.

# Example

 For startTag = "<button type='button' disabled>", the output should be "</button>";
 
 For startTag = "<i>", the output should be "</i>".
 
# Input/Output

 - `[input]` string `startTag`/`start_tag`

 - `[output]` a string
"""

def generate_end_tag(start_tag: str) -> str:
    """
    Generates the appropriate end tag for a given starting HTML tag.

    Parameters:
    - start_tag (str): The starting HTML tag.

    Returns:
    - str: The end tag corresponding to the given starting tag.
    """
    # Extract the tag name from the start tag
    tag_name = start_tag[1:].split(' ')[0].rstrip('>')
    
    # Construct the end tag
    end_tag = f"</{tag_name}>"
    
    return end_tag