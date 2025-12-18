"""
QUESTION:
Write a function called `get_author` that takes in a string parameter `title` representing the title of a book and returns the author of the book in uppercase. Ignore any leading or trailing whitespace in the title. If the title is empty or only consists of whitespace, return None. 

Assume a predefined mapping of titles to authors, where "Alice in Wonderland" maps to "LEWIS CARROLL" and "The Hobbit" maps to "J.R.R. TOLKIEN". The title will only contain alphabets, spaces, and punctuation marks. The title can have leading and trailing spaces, multiple spaces between words, and multiple punctuation marks at the end, but no punctuation marks in the middle of the title. The author name will only contain alphabets and spaces with no punctuation marks.
"""

def get_author(title):
    """
    Returns the author of a book given its title.

    Args:
    title (str): The title of the book.

    Returns:
    str or None: The author of the book in uppercase if title is valid, otherwise None.
    """
    title = title.strip()
    if not title:
        return None

    # Predefined mapping of titles to authors
    title_author_map = {
        "Alice in Wonderland": "LEWIS CARROLL",
        "The Hobbit": "J.R.R. TOLKIEN"
    }

    # Return the author of the book in uppercase
    return title_author_map.get(title.upper())