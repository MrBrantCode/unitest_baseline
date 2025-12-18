"""
QUESTION:
Create a function called `sort_slogans` that takes a dictionary of space companies as keys and their respective slogans as values. The function should return a list of tuples, where each tuple contains a company and its corresponding slogan. The list should be sorted by slogans in ascending order (case-insensitive), and if two or more slogans are the same, the companies should be sorted alphabetically. Additionally, the companies should be sorted in descending order based on the sum of the ASCII values of their characters.
"""

def sort_slogans(slogans):
    slogans_list = [(company, slogan) for company, slogan in slogans.items()]
    sorted_list = sorted(slogans_list, key=lambda x: (x[1].lower(), x[0]))
    return sorted(sorted_list, key=lambda x: sum(ord(c) for c in x[0]), reverse=True)