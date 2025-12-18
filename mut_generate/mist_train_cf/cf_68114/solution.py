"""
QUESTION:
Implement a function called `showAuthorDetails` that takes no parameters, which returns the author's name, birth date, and birth place. If the author's birth date or birth place is not available, the function should return a message stating that the specific detail is not available. The function should handle exceptions that may arise when the author's birth date and place are not available.
"""

def showAuthorDetails(author, birth_date=None, birth_place=None):
    author_details = f"Author: {author}\n"
    author_details += "Birth Date: Not Available\n" if birth_date is None else f"Birth Date: {birth_date}\n"
    author_details += "Birth Place: Not Available\n" if birth_place is None else f"Birth Place: {birth_place}\n"
    return author_details