"""
QUESTION:
Write a function named `solve_problem` that takes a two-dimensional list `lst` of length 'n' (where each sublist is of length 'm') and an integer `index` as input. The function should return two sorted lists: one sorted in descending order based on the sum of the elements in each sublist, and the other sorted based on the elements at the given `index` in each sublist.
"""

def solve_problem(lst, index):
    # Sorting the main list in descending order based on sum of sublist
    list_sorted_sum = sorted(lst, key=sum, reverse=True)
      
    # Sorting the main list based on a user-given index
    list_sorted_index = sorted(lst, key=lambda x: x[index])
    return list_sorted_sum, list_sorted_index