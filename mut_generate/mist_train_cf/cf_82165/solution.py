"""
QUESTION:
Create a function `sort_and_filter_books` that takes a list of dictionaries representing books, each with 'title', 'author', and 'publication_year' keys, and an optional 'year' parameter (defaulting to 1980). The function should remove duplicate books, filter out books published before the specified year, and sort the remaining books by publication year and the author's last name. The function should be efficient and accurate for large datasets.
"""

def sort_and_filter_books(books_list, year=1980):
    # remove duplicates
    books_set = set([tuple(book.items()) for book in books_list])
    # convert back to list of dictionaries
    books_unique = [dict(book) for book in books_set]
    # filter books published after a given year
    books_after_year = [book for book in books_unique if book['publication_year'] > year]

    # sort books by publication year and author's last name
    books_sorted = sorted(books_after_year, key=lambda i: (i['publication_year'], i['author'].split()[-1]))

    return books_sorted