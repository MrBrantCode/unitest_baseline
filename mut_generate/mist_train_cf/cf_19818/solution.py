"""
QUESTION:
Create a function `paginate_messages` that takes in a list of messages and the number of messages per page as arguments. It should return a list of pages where each page is a list of messages. The function should handle cases where the total number of messages is not a multiple of the number of messages per page.
"""

def paginate_messages(messages, messages_per_page):
    """
    Paginates a list of messages into multiple pages.

    Args:
    messages (list): The list of messages to be paginated.
    messages_per_page (int): The number of messages per page.

    Returns:
    list: A list of pages where each page is a list of messages.
    """
    return [messages[i:i + messages_per_page] for i in range(0, len(messages), messages_per_page)]