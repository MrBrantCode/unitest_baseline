"""
QUESTION:
Write a function `recommend_books` that takes two parameters: a dictionary `books` where keys are genres and values are lists of book titles, and a dictionary `publication_dates` where keys are book titles and values are publication years. The function should return a dictionary where keys are genres, values are dictionaries with two keys: `recommended_books` and `all_books`. For Fantasy genre, `recommended_books` should contain the book with the most recent publication date, and for Horror genre, it should contain the book with the oldest publication date. `all_books` should contain all books of the respective genre, sorted by publication date.
"""

def recommend_books(books, publication_dates):
    recommended_books = {}
    for genre, books_list in books.items():
        sorted_books = sorted(books_list, key=lambda x: publication_dates[x])
        if genre == "Fantasy":
            recommended_books[genre] = {
                "recommended_books": [sorted_books[-1]],
                "all_books": sorted_books
            }
        elif genre == "Horror":
            recommended_books[genre] = {
                "recommended_books": [sorted_books[0]],
                "all_books": sorted_books
            }
        else:
            recommended_books[genre] = {
                "recommended_books": [],
                "all_books": sorted_books
            }
    return recommended_books