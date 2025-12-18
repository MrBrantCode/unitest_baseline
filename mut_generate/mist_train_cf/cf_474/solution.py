"""
QUESTION:
Write a function `get_authors` that retrieves the names of authors whose last name starts with the letter "S" and have published at least 10 books. The function should return the results sorted in descending order based on the number of books published by each author.
"""

def get_authors(authors):
    """
    Retrieves the names of authors whose last name starts with the letter "S" 
    and have published at least 10 books.

    Args:
    authors (list): A list of dictionaries containing author information.
                    Each dictionary should have 'name' and 'books' or 'book_count' as keys.

    Returns:
    list: A list of author names sorted in descending order by the number of books published.
    """
    # Filter authors by last name starting with 'S' and having at least 10 books
    authors = [author for author in authors if author['name'].split()[-1].startswith('S') and author.get('books', author.get('book_count', 0)) >= 10]

    # Sort authors in descending order by the number of books published
    authors.sort(key=lambda x: x.get('books', x.get('book_count', 0)), reverse=True)

    # Return a list of author names
    return [author['name'] for author in authors]