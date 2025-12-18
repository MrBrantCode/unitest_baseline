"""
QUESTION:
Create a function `get_third_author_reversed` that takes a list of authors as input and returns the name of the third author in reverse order. The list of authors is a comma-separated string. The function should handle cases where there are less than three authors.
"""

def get_third_author_reversed(authors):
    authors_list = authors.split(',')
    if len(authors_list) < 3:
        return None
    else:
        third_author = authors_list[2].strip()
        return third_author[::-1]