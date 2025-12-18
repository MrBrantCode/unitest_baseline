"""
QUESTION:
Create a function called `recommend_books` that takes two parameters: `books` (a dictionary where keys are genres and values are lists of book titles) and `publication_dates` (a dictionary where keys are book titles and values are publication dates). The function should return a dictionary where keys are genres, and values are dictionaries containing two keys: "recommended_books" and "all_books". "recommended_books" should be a list containing the book with the most recent publication date for the Fantasy genre and the oldest for other genres, while "all_books" should be a list of all books in the genre sorted by publication date.
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
        else:
            recommended_books[genre] = {
                "recommended_books": [sorted_books[0]],
                "all_books": sorted_books
            }
    return recommended_books