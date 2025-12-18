"""
QUESTION:
Create a function `group_highly_rated` that takes a list of dictionaries representing novels, each containing a title, rating, and author. The function should return a dictionary where the keys are the authors and the values are lists containing the titles of their books with a rating of 4.5 or more. The function should efficiently handle multiple novels from the same author in the input list.
"""

def group_highly_rated(novels):
    result = {}
    for novel in novels:
        if novel['rating'] >= 4.5:
            if novel['author'] in result:
                result[novel['author']].append(novel['title'])
            else:
                result[novel['author']] = [novel['title']]
    return result