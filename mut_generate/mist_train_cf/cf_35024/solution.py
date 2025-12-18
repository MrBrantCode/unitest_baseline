"""
QUESTION:
Write a function `sort_authors_by_last_name` that takes a list of author names, where each name is in the format "First Name Last Name", and returns the list sorted alphabetically by the authors' last names. The input list is not empty and all names are strings in the specified format.
"""

def sort_authors_by_last_name(authors):
    return sorted(authors, key=lambda x: x.split()[-1])