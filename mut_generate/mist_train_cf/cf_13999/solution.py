"""
QUESTION:
Write a function called `sort_space_slogans` that takes a dictionary where keys are space company names and values are their respective slogans. The function should return a list of tuples containing the company and its slogan, sorted alphabetically by slogans in a case-insensitive manner. If two or more slogans are the same, the companies should be sorted alphabetically. The input dictionary can have an arbitrary number of key-value pairs.
"""

def sort_space_slogans(slogans):
    slogan_tuples = list(slogans.items())
    sorted_tuples = sorted(slogan_tuples, key=lambda x: (x[1].lower(), x[0]))
    return sorted_tuples