"""
QUESTION:
Create a function `library_catalog(books)` that takes a list of tuples as input, where each tuple contains a book title and its author in the format `(title, author)`. The function should then return another function `search_book(query)` that takes a string `query` as input. The `search_book(query)` function should search for books by either title or author and return the title and author of the book if found, or a message indicating that the book is not in the catalog.
"""

def library_catalog(books):
    catalog = {title: author for title, author in books}

    def search_book(query):
        if query in catalog:
            return f'"{query}" by {catalog[query]}'
        else:
            for title, author in catalog.items():
                if query == author:
                    return f'"{title}" by {author}'
            return "Book not in catalog"

    return search_book