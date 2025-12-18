"""
QUESTION:
Create a function called `recommend_books_by_genre` that takes in a dictionary of genres with corresponding book titles and a dictionary of publication dates for each book. The function should return a dictionary where each key is a genre and the value is another dictionary containing two keys: "recommended_books" and "all_books". "recommended_books" should contain a list with the most recent book for Fantasy and the oldest book for Horror, and "all_books" should contain a list of all books in the genre, sorted by publication date. The function should handle the genres "Fantasy" and "Horror".
"""

def recommend_books_by_genre(genres, publication_dates):
    recommended_books = {}
    for genre, books_list in genres.items():
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
    return recommended_books