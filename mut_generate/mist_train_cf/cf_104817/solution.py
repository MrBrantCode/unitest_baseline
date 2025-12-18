"""
QUESTION:
Create a function called `rank_languages` that takes a list of dictionaries, where each dictionary contains information about a programming language, including its name, release year, and other relevant details. The function should rank these languages based on their release year and return the ranked list.
"""

def rank_languages(languages):
    return sorted(languages, key=lambda x: x['release_year'])