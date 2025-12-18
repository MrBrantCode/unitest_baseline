"""
QUESTION:
Create a function called `get_author` that takes a string parameter `title` representing the title of a book, strips any leading or trailing whitespace, and returns the author of the book. If the title is empty after stripping, the function should return `None`. The function should be able to handle multiple book titles and their respective authors.
"""

def get_author(title):
    title = title.strip()
    if title == "":
        return None
    elif title == "Alice in Wonderland":
        return "Lewis Carroll"
    elif title == "The Hobbit":
        return "J.R.R. Tolkien"
    # Add more elif statements for other book titles and their respective authors