"""
QUESTION:
Implement a function `get_books` that retrieves a list of books based on query parameters. The function should take in `author`, `genre`, `publication_year`, `sort`, `page`, and `page_size` as parameters. It should filter books by `author`, `genre`, and `publication_year` if provided, sort the results by the specified field in ascending or descending order, and paginate the results based on the provided `page` and `page_size`. The function should return a dictionary containing the current page number, page size, total number of books, and a list of books.
"""

def get_books(author=None, genre=None, publication_year=None, sort=None, page=1, page_size=10):
    # Assuming a list of books is stored in this variable
    books = [
        {"id": "1234", "title": "Book 1", "author": "Author 1", "genre": "Genre 1", "publicationYear": 2020},
        {"id": "5678", "title": "Book 2", "author": "Author 2", "genre": "Genre 2", "publicationYear": 2021},
        # Add more books here...
    ]

    # Filter books by author, genre, and publication year
    filtered_books = [book for book in books if (not author or book["author"] == author) and (not genre or book["genre"] == genre) and (not publication_year or book["publicationYear"] == publication_year)]

    # Sort books by the specified field in ascending or descending order
    if sort:
        field, order = sort.split(":")
        if order == "asc":
            filtered_books.sort(key=lambda book: book[field])
        elif order == "desc":
            filtered_books.sort(key=lambda book: book[field], reverse=True)

    # Paginate the results
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    paginated_books = filtered_books[start_index:end_index]

    # Return a dictionary containing the current page number, page size, total number of books, and a list of books
    return {
        "page": page,
        "pageSize": page_size,
        "total": len(filtered_books),
        "books": paginated_books
    }