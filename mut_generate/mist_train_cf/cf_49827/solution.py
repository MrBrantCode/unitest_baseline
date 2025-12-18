"""
QUESTION:
Write a function named `remove_duplicates` that takes a list as input and returns a tuple. The first element of the tuple should be the input list with duplicates removed, maintaining the original order of non-duplicate elements. The second element should be the total number of duplicates removed.
"""

def remove_duplicates(lst):
    unique_lst = []
    duplicates_count = 0

    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
        else:
            duplicates_count += 1

    return unique_lst, duplicates_count