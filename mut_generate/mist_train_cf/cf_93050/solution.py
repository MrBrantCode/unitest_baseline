"""
QUESTION:
Write a function named `sort_space_slogans` that takes a dictionary with company names as keys and their corresponding slogans as values. The function should return a list of tuples, each containing a company and its slogan, sorted by slogans in ascending order (case-insensitive) and then by company names in ascending order if the slogans are the same.
"""

def sort_space_slogans(slogans):
    slogan_tuples = list(slogans.items())
    sorted_tuples = sorted(slogan_tuples, key=lambda x: (x[1].lower(), x[0]))
    return sorted_tuples