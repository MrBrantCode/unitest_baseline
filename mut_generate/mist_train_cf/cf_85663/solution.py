"""
QUESTION:
Create a function called `extract_html_mime_type` that recursively traverses a given email structure to find and return the content of the first part with the MIME type `text/html`. The email structure can be a nested hierarchy of MIME types where 'multipart' types are containers for other MIME types.
"""

from email.message import Message

def extract_html_mime_type(message: Message) -> str:
    """
    Recursively traverses a given email structure to find and return the content of the first part with the MIME type 'text/html'.

    Args:
    message (Message): The email message structure.

    Returns:
    str: The content of the first part with the MIME type 'text/html' or None if not found.
    """

    # Check if the message is of type 'text/html'
    if message.get_content_type() == 'text/html':
        return message.get_payload()

    # If the message is of type 'multipart', recursively search its parts
    elif message.get_content_type().startswith('multipart'):
        for part in message.get_payload():
            content = extract_html_mime_type(part)
            if content is not None:
                return content

    # If no 'text/html' part is found, return None
    return None