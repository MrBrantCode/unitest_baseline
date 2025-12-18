"""
QUESTION:
Write a function, `find_top_authors_by_year`, that finds the author with the highest number of books published in each year, excluding any authors who have published less than 5 books in that year. The function should return the year, author, and the average rating of the books published by each author in the respective year.
"""

from collections import defaultdict
from statistics import mean

def find_top_authors_by_year(books):
    authors_by_year = defaultdict(dict)
    for book in books:
        if book['author'] not in authors_by_year[book['year']]:
            authors_by_year[book['year']][book['author']] = []
        authors_by_year[book['year']][book['author']].append(book['rating'])

    result = []
    for year, authors in authors_by_year.items():
        top_author = max(authors, key=lambda author: len(authors[author]))
        if len(authors[top_author]) >= 5:
            result.append({
                'year': year,
                'author': top_author,
                'average_rating': mean(authors[top_author])
            })

    return result