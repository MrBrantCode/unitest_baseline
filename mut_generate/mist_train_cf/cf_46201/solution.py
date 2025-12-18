"""
QUESTION:
Create a function `isolate_books_after_year` that takes a list of books and a year as input, where each book is represented as a dictionary containing a list of editions, each with a 'year' key. The function should return a list of books with their first edition published after the given year. Assume all years are in the Gregorian calendar and in YYYY format.
"""

def isolate_books_after_year(books, year):
    isolated_books = []
    
    for book in books:
        editions = book.get('editions', [])
        
        # Assuming edition's year is in YYYY format, we sort it from earlier to later
        editions.sort(key=lambda edition: edition.get('year', '9999'))

        first_year = int(editions[0].get('year', 0)) if editions else 0
        
        if first_year > year:
            isolated_books.append(book)

    return isolated_books