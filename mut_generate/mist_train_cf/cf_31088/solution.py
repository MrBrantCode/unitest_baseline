"""
QUESTION:
Implement the `get_paginated_books` and `get_context_data` methods in the `BookMyListView` class. The `get_paginated_books` method should take a `page_number` as input, divide the list of books into blocks of size `block_size`, and then chunk each block into lists of size `chunk_size`. The `get_context_data` method should include the paginated books in the context data, where the current page number is obtained from the request parameters. The `block_size` and `chunk_size` are instance variables initialized with values from the `book_settings` module.
"""

def get_paginated_books(queryset, page_number, block_size, chunk_size):
    """
    Divide the list of books into blocks of size `block_size`, 
    then chunk each block into lists of size `chunk_size`.
    
    Args:
    queryset (list): The list of books to be paginated.
    page_number (int): The current page number.
    block_size (int): The size of each block.
    chunk_size (int): The size of each chunk.
    
    Returns:
    list: The paginated books.
    """
    start_index = (page_number - 1) * block_size
    end_index = start_index + block_size
    paginated_books = queryset[start_index:end_index]
    chunked_books = [paginated_books[i:i + chunk_size] for i in range(0, len(paginated_books), chunk_size)]
    return chunked_books