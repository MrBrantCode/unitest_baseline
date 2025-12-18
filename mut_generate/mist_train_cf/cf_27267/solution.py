"""
QUESTION:
Implement a function `detectAtMe` that takes two parameters: `nameInGroup` (the name of the chatbot in the group) and `content` (the message content). The function should check if the chatbot is mentioned in the message content and modify the content accordingly. If the chatbot is mentioned, prepend `[@ME]` to the message content and remove the mention of the chatbot. If the chatbot is not mentioned, leave the message content unchanged. Return the modified message content.
"""

def detectAtMe(nameInGroup, content):
    """
    Check if the chatbot is mentioned in the message content and modify the content accordingly.

    Args:
    nameInGroup (str): The name of the chatbot in the group.
    content (str): The message content.

    Returns:
    str: The modified message content with `[@ME]` prepended if the chatbot is mentioned, otherwise the original message content.
    """
    if '@' + nameInGroup in content:
        modified_content = '[@ME] ' + content.replace('@'+nameInGroup, '')
        return modified_content
    else:
        return content