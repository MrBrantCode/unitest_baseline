"""
QUESTION:
Write a function `get_author_info` that retrieves author names who have published at least 3 books with the topic 'Artificial Intelligence', along with the total number of books published, average rating, and total copies sold for each author. The results should be sorted in descending order by average rating, then by the number of books published, and finally by total copies sold.
"""

def get_author_info(authors, books):
    """
    Retrieves author names who have published at least 3 books with the topic 'Artificial Intelligence',
    along with the total number of books published, average rating, and total copies sold for each author.

    Args:
        authors (list): A list of dictionaries containing author information.
        books (list): A list of dictionaries containing book information.

    Returns:
        list: A list of dictionaries containing author information, sorted in descending order by average rating,
              then by the number of books published, and finally by total copies sold.
    """

    # Create a dictionary to store author information
    author_info = {}

    # Iterate over each book
    for book in books:
        # Check if the book's topic is 'Artificial Intelligence'
        if book['topic'] == 'Artificial Intelligence':
            # Get the author's name
            author_name = next((author['author_name'] for author in authors if author['author_id'] == book['author_id']), None)

            # If the author is not already in the dictionary, add them
            if author_name not in author_info:
                author_info[author_name] = {'total_books_published': 0, 'total_rating': 0, 'total_copies_sold': 0}

            # Increment the author's total books published, rating, and copies sold
            author_info[author_name]['total_books_published'] += 1
            author_info[author_name]['total_rating'] += book['rating']
            author_info[author_name]['total_copies_sold'] += book['copies_sold']

    # Filter authors who have published at least 3 books and calculate average rating
    author_info = {author: info for author, info in author_info.items() if info['total_books_published'] >= 3}
    for author, info in author_info.items():
        info['average_rating'] = info['total_rating'] / info['total_books_published']

    # Sort authors by average rating, total books published, and total copies sold
    sorted_authors = sorted(author_info.items(), key=lambda x: (-x[1]['average_rating'], -x[1]['total_books_published'], -x[1]['total_copies_sold']))

    # Format the output
    result = []
    for author, info in sorted_authors:
        result.append({
            'author_name': author,
            'total_books_published': info['total_books_published'],
            'average_rating': info['average_rating'],
            'total_copies_sold': info['total_copies_sold']
        })

    return result