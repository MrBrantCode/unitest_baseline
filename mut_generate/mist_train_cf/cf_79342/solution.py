"""
QUESTION:
Write a function `filter_novels` that takes a list of dictionaries, where each dictionary represents a novel with a "title" and a "rating". The function should return a new list containing only the novels with a rating of 4.5 or higher.
"""

def filter_novels(novels):
    high_rated_novels = [novel for novel in novels if novel["rating"] >= 4.5]
    return high_rated_novels