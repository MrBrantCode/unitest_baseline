"""
QUESTION:
Create a function named `rank_tuples` that ranks a list of tuples based on the character length of the second element within each tuple. The function should take a list of tuples as input and return the sorted list. The tuples are to be sorted in ascending order by default, but should also have the option to sort in descending order.
"""

def rank_tuples(tuples_list, reverse=False):
    return sorted(tuples_list, key=lambda x: len(x[1]), reverse=reverse)