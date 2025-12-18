"""
QUESTION:
Implement a function called "showAuthor" in a class that takes in an author's name and a database of authors and their works. The function should return a formatted string containing the author's name and their other works. The database is a dictionary where the keys are author names and the values are lists of their works. The function should be efficient and able to handle a large database.
"""

def showAuthor(author, database):
    other_works = database.get(author, [])
    other_works_str = ', '.join([work for work in other_works if work != author])

    return f"Author: {author}\nOther works: {other_works_str or 'N/A'}"