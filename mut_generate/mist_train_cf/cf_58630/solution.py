"""
QUESTION:
Write a function `check_list_sorting` that takes a list as input and returns a dictionary. The input list can contain nested lists and diverse data types. The function should verify the sorting order of each nested list individually and return a dictionary where each key is the index of the nested list in the main list and the value is the sorting order of that nested list ('ascending', 'descending', or 'unsorted'). If a TypeError occurs due to the presence of different data types, the function should return 'unsorted - TypeError' for the corresponding nested list.
"""

def check_list_sorting(lst):
    sort_dict = {}
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            try:
                if all(lst[i][j] <= lst[i][j+1] for j in range(len(lst[i])-1)):
                    sort_dict[i] = 'ascending'
                elif all(lst[i][j] >= lst[i][j+1] for j in range(len(lst[i])-1)):
                    sort_dict[i] = 'descending'
                else:
                    sort_dict[i] = 'unsorted'
            except TypeError:
                sort_dict[i] = 'unsorted - TypeError'
            
    return sort_dict