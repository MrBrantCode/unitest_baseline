"""
QUESTION:
Write a function `count_name_occurrences(names, book_tags)` that takes a list of names and a sequence of strings as input, and returns a dictionary containing the count of occurrences of each name in the sequence. The function should initialize the dictionary with all names from the input list as keys, and their counts set to 0. It should then iterate over the sequence, incrementing the count for each occurrence of a name from the input list. The function should return the dictionary containing the final counts.
"""

def count_name_occurrences(names, book_tags):
    name_counts = {name: 0 for name in names}
    for tag in book_tags:
        if tag in name_counts:
            name_counts[tag] += 1
    return name_counts